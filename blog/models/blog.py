from django.db import models
from .category import Category
from .myuser import MyUser
from taggit.managers import TaggableManager
from django_quill.fields import QuillField

class Blog(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    description = QuillField()
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    category_id = models.ForeignKey('Category', on_delete=models.CASCADE)
    user_id = models.ForeignKey('MyUser', on_delete=models.CASCADE)
    tag = TaggableManager()
    views = models.PositiveBigIntegerField(default=0)
    img = models.ImageField(upload_to='user/', default=True)

    def __str__(self):
        return self.name
