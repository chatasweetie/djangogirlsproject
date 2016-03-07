from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    """makes a Post model"""
    class Meta:
        model = Post
        fields = ('title', 'text',)
