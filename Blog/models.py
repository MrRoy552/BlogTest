from django.db import models
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
from setuptools import Require

from .managers import CustomUserManager

    

# Admin models here.
class User(AbstractUser):

    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=50, blank=True)
    mobileNumber=models.CharField(max_length=12,blank=True,null=False)
    is_active = models.BooleanField(default=True)
    is_deleted = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)
    modified_date = models.DateTimeField(default=timezone.now)
    created_by = models.EmailField()
    modified_by = models.EmailField()
    is_verified=models.BooleanField(default=False)
    username=models.CharField(max_length=30)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
    
class Blog(models.Model):
    Author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='article')
    Titel=models.CharField(max_length=200)
    Body=models.TextField()
    created_At = models.DateTimeField(default=timezone.now)
    updated_At = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.Titel
