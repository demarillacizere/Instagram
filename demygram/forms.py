from django import forms
from .models import Post,Comment, Profile

class AddProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user', 'date_posted','profile','like']

class NewCommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        exclude = ['post', 'user', 'date_posted']