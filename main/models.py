from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=200, null=True)
    content = models.TextField(null=True)
    time = models.DateTimeField(default=timezone.now, null=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200, null=True)
    time = models.DateTimeField(default=timezone.now, null=True)
    parent = models.ForeignKey(
        'self', related_name="reply", on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment
