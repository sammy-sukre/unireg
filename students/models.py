from django.db import models
from django.contrib.auth.models import User

class user(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email = models.EmailField(max_length=150, blank=False)
    course = models.CharField(max_length=20, blank = False, null = False)
    
