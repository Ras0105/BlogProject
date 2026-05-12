from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    # Use PROTECT so deleting a category doesn't silently wipe posts
    category = models.ForeignKey(
        Category, on_delete=models.PROTECT, related_name='posts'
    )
    # Track who wrote the post; null=True so existing posts aren't broken
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL, null=True, blank=True, related_name='posts'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=100)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author}: {self.text[:50]}"
