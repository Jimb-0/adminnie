from django.db import models
from django.contrib.auth.models import User


class UserProfileInfo(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)  #extends User model - already has username email first name last and password

    #additional
    portfolio_site = models.URLField(blank=True) #required=false equivalent
    profile_pic = models.ImageField(upload_to='profile_pics',blank=True)

    def __str__(self):      #method
        return self.user.username


# Create your models here.
