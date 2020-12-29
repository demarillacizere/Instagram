from django import forms
from .models import Post

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date_posted']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['user', 'date_posted']