from django import forms
from .models import Post,Comment

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date_posted','profile','like']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'user', 'date_posted']