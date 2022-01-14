from django import forms
from .models import Blog, Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text']

class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ('name', 'slug', 'description', 'category_id', 'tag', 'img')