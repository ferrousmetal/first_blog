from django.db import models


class Comments(models.Model):
    name = models.CharField(max_length=100, verbose_name='姓名')
    email = models.EmailField(max_length=50, verbose_name='邮箱')
    url = models.URLField(blank=True, verbose_name='个人网站')
    text = models.TextField(verbose_name='评论')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, verbose_name='评论文章')

    def __str__(self):
        return self.text[:20]

    class Meta:
        verbose_name = "评论"
        verbose_name_plural = verbose_name
        ordering = ("created_time",)
