import markdown
from django.shortcuts import render, get_object_or_404
from blog.models import *
from comments.forms import *
from django.db.models import Q
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def index(request):
    posts = Post.objects.all()
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'index.html', locals())


def detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()
    post.content = markdown.markdown(post.content,
                                     extensions=[
                                         'markdown.extensions.extra',
                                         'markdown.extensions.codehilite',
                                         'markdown.extensions.toc',
                                     ])
    form = CommentForm()
    comment_list = post.comments_set.all()
    # comment_list = Comments.objects.filter(post=post)

    context = {'post': post,
               'form': form,
               'comment_list': comment_list
               }
    return render(request, 'detail.html', locals())


def archives(request, year, month):
    posts = Post.objects.filter(created_time__year=year)  # , created_time__month=month
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'index.html', context={'post_list': post_list})


def category(request, pk):
    cate = get_object_or_404(Category, pk=pk)
    posts = Post.objects.filter(category=cate)
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'index.html', context={'post_list': post_list})


def tag(request, pk):
    tag = get_object_or_404(Tag, pk=pk)
    posts = Post.objects.filter(tag=tag)
    page = request.GET.get('page')
    paginator = Paginator(posts, 5)
    try:
        post_list = paginator.page(page)
    except PageNotAnInteger:
        post_list = paginator.page(1)
    return render(request, 'index.html', context={'post_list': post_list})


def search(request):
    q = request.GET.get('q')
    error_msg = ''

    if not q:
        error_msg = "请输入关键词"
        return render(request, 'index.html', {'error_msg': error_msg})

    post_list = Post.objects.filter(Q(title__icontains=q) | Q(content__icontains=q))
    return render(request, 'index.html', locals())


def about(request):
    return render(request, 'about.html')
