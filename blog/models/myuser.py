from django.db import models
from django.contrib.auth.models import AbstractUser

class MyUser(AbstractUser):
    bio = models.CharField(max_length = 200, blank=True)
    location = models.CharField(max_length=30, blank=True)
    birth_date = models.DateTimeField(null = True, blank=True)
    img = models.ImageField(upload_to='users/', blank=True, null=True)
    facebook_link = models.URLField(max_length=200, blank=True, null=True)
    instagram_link = models.URLField(max_length=200, blank=True, null=True)
    youtube_link = models.URLField(max_length=200, blank=True, null=True)
    telegram_link = models.URLField(max_length=200, blank=True, null=True)
    gitHub_link = models.URLField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.username