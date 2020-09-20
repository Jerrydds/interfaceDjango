from django.db import models
from django.utils import timezone


# 添加评论数据表
class Comment(models.Model):
    # 添加名字 列名
    name = models.CharField('名字', max_length=50)
    # 添加邮箱
    email = models.EmailField('邮箱')
    # 添加网址
    url = models.URLField('网址', blank=True)
    # 添加内容
    text = models.TextField('内容')
    # 添加 创建时间
    created_time = models.DateTimeField('创建时间', default=timezone.now)
    # 添加 文章
    post = models.ForeignKey('web.Post', verbose_name='文章', on_delete=models.CASCADE)

    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering = ['-created_time']

    def __str__(self):
        return '{}: {}'.format(self.name, self.text[:20])
