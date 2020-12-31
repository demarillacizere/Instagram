from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Post,Comment
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewCommentForm

@login_required(login_url='/accounts/login/')
def insta(request):
    posts = Post.objects.order_by('-date_posted')
    comments = Comment.objects.all()
    return render(request, 'index.html', {"posts": posts, 'comments':comments})


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

@login_required(login_url='/accounts/login/')
def single_post(request, post_id):
    post = Post.objects.get(pk=post_id)
    comments = Comment.get_comments_by_post(post_id).order_by('-date_posted')
    current_user = request.user
    if request.method == 'POST':
        form = NewCommentForm(request.POST)
        if form.is_valid():
            new_comment = form.save(commit=False)
            new_comment.user = current_user
            new_comment.post = post
            new_comment.save()
            return redirect('single_post',post_id=post_id)
    else:
        form = NewCommentForm()
        
    return render(request, 'post.html', {'post':post, 'form':form,'comments':comments})    
