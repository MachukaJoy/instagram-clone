from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
# Create your models here.
class Profile(models.Model):
    name = models.CharField(max_length=30)
    profile_pic = CloudinaryField('images')
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE, default='', null=True)

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    def __str__(self):
        return f'{self.user.username} Profile'

class  Post(models.Model):
    image = CloudinaryField('images')
    title = models.CharField(max_length=30, default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE, default='', null=True)
    caption = models.TextField(max_length=300)

    @classmethod
    def all_posts(cls) :
        posts = cls.objects.all()
        return posts

    def __str__(self):
        return self.title 