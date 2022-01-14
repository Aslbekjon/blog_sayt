from django.db import models
from .blog import Blog
from .myuser import MyUser

class Comment(models.Model):
    blog_id = models.ForeignKey('Blog', on_delete = models.CASCADE)
    user_id = models.ForeignKey('MyUser', on_delete = models.CASCADE)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.text