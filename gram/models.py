from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
# Create your models here.
class Profile(models.Model):
    name =  models.CharField(max_length = 30)
    profile_pic = CloudinaryField('images')
    bio = models.TextField()

    def __str__(self):
        return self.name


    def save_profile(self):
        self.save()