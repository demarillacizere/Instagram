from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewCommentForm

@login_required(login_url='/accounts/login/')
def insta(request):
    posts = Post.objects.all()
    return render(request, 'index.html', {"posts": posts})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.save()
        return redirect('insta')

    else:
        form = NewPostForm()
    return render(request, 'new_post.html', {"form": form})
