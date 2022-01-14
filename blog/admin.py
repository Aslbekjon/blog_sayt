from django.contrib import admin
from .models import Category, Blog, MyUser, Comment
# Register your models here.

admin.site.register([Category, Blog, MyUser, Comment])