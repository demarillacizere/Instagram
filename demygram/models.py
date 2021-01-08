from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,null=True)
    profile_photo= models.ImageField(upload_to='profiles/',null=True)
    bio= models.CharField(max_length=140, null=True)


    def save_profile(self):
        self.save()

    @classmethod
    def get_profile(cls, user):
        profile = cls.objects.filter(user=user).first()
        return profile

    @classmethod
    def get_profile_id(cls, user):
        profile = cls.objects.get(pk =user)
        return profile

    @classmethod
    def find_profile(cls,search_term):
        profile = Profile.objects.filter(user__username__icontains=search_term)
        return profile

    class Meta:
        ordering = ['user']

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/')
    caption = models.CharField(max_length =240)
    location = models.CharField(max_length =30)
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null = True)
    like = models.IntegerField(default=0)
    def __str__(self):
        return self.caption

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    @classmethod
    def update_post(cls, id ,post_image, caption , location):
        update = cls.objects.filter(id = id).update(post_image = post_image, caption = caption ,location = location)
    
    @classmethod
    def get_posts_by_id(cls, id):
        posts = cls.objects.filter(profile = id).all()
        return posts

    class Meta:
        ordering = ['caption']

class Comment(models.Model):
    comment= models.CharField(max_length =30)
    date_posted = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        'Post',
        on_delete=models.CASCADE,
        )
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    count = models.IntegerField(default=0)
    def __str__(self):
        return self.user

    def save_comment(self):
        self.save()

    def delete_comment(self):
        self.delete()
    
    @classmethod
    def update_post(cls, id ,comment):
        update = cls.objects.filter(id = id).update(comment = comment)
    
    @classmethod
    def get_comments_by_post(cls, id):
        comments = Comment.objects.filter(post__pk = id)
        return comments
    class Meta:
        ordering = ['comment']

class Follow(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    profile = models.ForeignKey(Profile,on_delete=models.CASCADE, null=True)

    @classmethod
    def get_followers(cls, user):
        followers = cls.objects.filter(user=user).all()
        return followers

    class Meta:
        ordering = ['user']