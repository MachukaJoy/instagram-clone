from django.test import TestCase
from .models import Profile

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
        name = Profile.objects.all()


