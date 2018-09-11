from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


class User(AbstractUser):
    qq = models.CharField(max_length=20, verbose_name="QQ号")
    tel = models.CharField(max_length=15, verbose_name="电话")

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ("id",)


class Category(models.Model):
    name = models.CharField(max_length=20, verbose_name='分类名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "分类"
        verbose_name_plural = verbose_name
        ordering = ("id",)


class Tag(models.Model):
    name = models.CharField(max_length=20, verbose_name='标签名')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "标签"
        verbose_name_plural = verbose_name
        ordering = ("id",)


class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name='文章标题')
    content = models.TextField(verbose_name='文章内容')
    created_time = models.DateTimeField(verbose_name='创建时间')
    modified_time = models.DateTimeField(verbose_name='最后一次修改时间')
    excerpt = models.CharField(max_length=200, blank=True, verbose_name='文章摘要')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='文章类型')
    tag = models.ManyToManyField(Tag, blank=True, verbose_name='文章标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='文章作者')
    views = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1
        self.save(update_fields=['views'])

    class Meta:
        verbose_name = "文章"
        verbose_name_plural = verbose_name
        ordering = ("-created_time", "-id")
