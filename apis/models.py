from django.db import models
from django.contrib.auth.models import User
from rest_framework import permissions
from rest_framework_simplejwt import authentication


class Tasks(models.Model):
    # permission_classes = (permissions.IsAuthenticated,)
    # authentication_classes = (authentication.JWTAuthentication,)
    title= models.CharField(max_length=100 ,blank=False, null=False)
    description= models.CharField(max_length=200 ,blank=False, null=False)
    is_completed=models.BooleanField(default=False,blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
