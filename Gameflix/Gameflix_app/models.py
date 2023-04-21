from django.contrib.auth.models import AbstractUser
from django.db import models
from .validators import file_size
from os import path


class User(AbstractUser):
    image = models.ImageField(upload_to='profile_images/',
                              height_field=None,
                              width_field=None,
                              max_length=100,
                              default='default/default.jpg')



class Video(models.Model):
    author = models.ForeignKey(User, related_name='new_video', on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/%y.%m.%d', validators=[file_size])

    def __str__(self):
        return self.title



class Comments(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    content = models.TextField()

