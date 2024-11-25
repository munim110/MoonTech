from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20, blank=True, null=True)
    address = models.TextField(null=True, blank=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    profile_pic = models.ImageField(upload_to='profile_pics/', default='profile_pics/default.jpeg')
    
    def __str__(self):
        return self.user.username