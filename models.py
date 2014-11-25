from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    picture = models.ImageField(upload_to='profile_images', blank = True)

    def __unicode__(self):
        return self.user.username
		
class UserPhoto0(models.Model):
    picture = models.ImageField(upload_to='profile_images', blank = False)
	