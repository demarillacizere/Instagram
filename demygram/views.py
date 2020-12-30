from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewCommentForm

@login_required(login_url='/accounts/login/')
def insta(request):
    new_comment = None
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = current_user
            new_comment.save()
            return redirect('insta')
    else:
        form = NewCommentForm()
    date = dt.date.today()
    posts = Post.objects.all()
    for post in posts:
        comments = Comment.objects.all().order_by('-date_posted')
    return render(request, 'index.html', {"posts": posts, "form": form,'comments':comments})


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
