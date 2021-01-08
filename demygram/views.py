from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404,HttpResponseRedirect
import datetime as dt
from .models import Post,Comment,Follow,Profile
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm, NewCommentForm, AddProfileForm
from django.contrib.auth.models import User

def signup(request):
    if request.user.is_authenticated():
        return redirect('home')
    else:
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                user = form.save(commit=False)
                user.save()
                new_profile = Profile(user=user)
        else:
            form = SignupForm()
    return render(request, 'registration/registration_form.html',{'form':form})


@login_required(login_url='/accounts/login/')
def insta(request):
    users = User.objects.all()
    current_user = request.user
    comments = Comment.objects.all()
    posts = Post.objects.all()
    my_profile = Profile.get_profile(current_user)
    following = Follow.get_followers(current_user)
    for post in posts:
        if request.method=='POST' and 'post' in request.POST:
            posted=request.POST.get("post")
            for post in posts:
                if (int(post.id)==int(posted)):
                    post.like+=1
                    post.save()
            return redirect('insta')
    return render(request, 'index.html', {"posts": posts, 'comments':comments,'users':users,'user':current_user,'my_profile':my_profile,'following':following})


@login_required(login_url='/accounts/login/')
def new_post(request):
    current_user = request.user
    profile = Profile.get_profile(current_user)
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = current_user
            post.profile = profile
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
    count = Comment.get_comments_by_post(post_id).count
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
        
    return render(request, 'post.html', {'post':post, 'form':form,'comments':comments,'count':count})    

@login_required(login_url='/accounts/login/')
def my_profile(request):
    current_user = request.user
    profile = Profile.objects.get(user=current_user)
    if profile == None:
        return redirect('add_profile')
    else:
        posts = Post.get_posts_by_id(profile.id)
    return render(request, 'profile.html', {"posts": posts, "profile": profile})

@login_required(login_url='/accounts/login/')
def add_profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = AddProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('my_profile')

    else:
        form = AddProfileForm()
    return render(request, 'add_profile.html', {"form": form})


@login_required(login_url='/accounts/login/')
def search_results(request):
    if 'user' in request.GET and request.GET["user"]:
        search_term = request.GET.get("user")
        profiles = Profile.find_profile(search_term)
        message = f"{search_term}"
        
        return render(request, 'search.html',{"results": profiles, "message":message})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def profile(request, profile_id):
    profile = Profile.get_profile_id(profile_id)
    posts = Post.objects.filter(profile=profile.id)
    count = Post.objects.filter(profile=profile).count
    comments = Comment.objects.all()
    for post in posts:
        if request.method=='POST' and 'comment' in request.POST:
            comment=Comment(comment=request.POST.get("comment"),
                            post=int(request.POST.get("post")),
                            user=request.POST.get("user"),
                            count=0)
            comment.save()
            comment.count=F('count')+1
            return redirect('profile',profile_id)
        if request.method=='POST' and 'post' in request.POST:
            posted=request.POST.get("post")
            for post in posts:
                if (int(post.id)==int(posted)):
                    post.like+=1
                    post.save()
            return redirect('profile', profile_id)
    return render(request, 'user_profile.html', {"posts": posts, "profile": profile, 'count':count,'comments':comments})


@login_required(login_url='/accounts/login/')
def follow(request, profile_id):
    current_user = request.user
    profile = Profile.get_profile_id(profile_id)
    follow_user = Follow(user=current_user, profile=profile)
    follow_user.save()
    myprofile_id= str(profile.id)
    return redirect('insta')