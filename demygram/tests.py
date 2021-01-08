from django.test import TestCase

from .models import *

class ProfileTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='maddi')
        self.profile = Profile.objects.create(user = self.user,bio = 'sassy')

    def test_instance(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_save_profile(self):
        self.assertTrue(isinstance(self.profile,Profile))

    def test_get_profile(self):
        self.profile.save()
        profile = Profile.get_profile()
        self.assertTrue(len(profile) > 0)

    def test_find_profile(self):
        self.profile.save()
        profile = Profile.find_profile('maddi')
        self.assertTrue(len(profile) > 0)

class PostTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(id = 1, username='maddi')
        self.profile = Profile.objects.create(user = self.user,bio = 'sassy')

        self.post = Post.objects.create(posted_by = self.user,
                                          profile = self.profile,
                                          caption ='turn up',
                                          likes = 0)

    def test_instance(self):
        self.assertTrue(isinstance(self.post,Post))

    def test_get_posts(self):
        self.post.save()
        post = Post.get_posts()
        self.assertTrue(len(post) == 1)



class CommentTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(id = 1, username='maddi')

        self.comment= Comment.objects.create(poster= self.user, comment='comment' )

    def test_instance(self):
        self.assertTrue(isinstance(self.comment, Comment))

    def test_save_comment(self):
        self.assertTrue(isinstance(self.comment,Comment))

    def test_get_comment(self):
        self.comment.save()
        comment = Comment.get_comment()
        self.assertTrue(len(comment) == 1)
