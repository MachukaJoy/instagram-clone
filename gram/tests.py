from django.test import TestCase
from .models import Profile, Post

# Create your tests here.
class ProfileTestClass(TestCase):

    def setUp(self):
        self.Machuka = Profile(name = 'msmachuka', profile_pic = 'image.jpeg', bio='Coder and living life')
        self.Machuka.save()

    def tearDown(self):
        Profile.objects.all().delete()


    def test_instance(self):
        self.assertTrue(isinstance(self.Machuka, Profile))

    def test_save_profile(self):
        self.Machuka.save_profile()
        self.Machuka = Profile.objects.all()

    def test_delete_method(self):
        self.Machuka.save_profile()
        self.Machuka.delete_user()

class PostTestCase(TestCase):
    def setUp(self):
        self.new_post = Post(image='image.jpeg', title='new_post', caption ='coder')
        self.new_post.save()

    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def  test_save_post(self):
        self.new_post.save_post()
        self.new_post = Post.objects.all()

    def test_delete_post(self):
        self.new_post.save_post()
        self.new_post.delete_post()

