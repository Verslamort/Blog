from django.contrib.auth.models import User
from django.db import models


class BlogPost(models.Model):
    """博客页面"""
    title = models.CharField(max_length=200)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'BlogPost'

    def __str__(self):
        """返回模型字符串表示"""
        return self.text

