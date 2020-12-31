from django.db import models
import datetime as dt
from tinymce.models import HTMLField
from django.contrib.auth.models import User

class Post(models.Model):
    post_image = models.ImageField(upload_to = 'posts/')
    caption = models.TextField()
    location = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return self.caption

    def save_post(self):
        self.save()

    def delete_post(self):
        self.delete()
    
    @classmethod
    def update_post(cls, id ,post_image, caption , location):
        update = cls.objects.filter(id = id).update(post_image = post_image, caption = caption ,location = location)
    

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

    def __str__(self):
        return self.comment

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
