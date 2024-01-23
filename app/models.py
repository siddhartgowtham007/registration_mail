from django.db import models

# Create your models here.
from django.contrib.auth.models import User

class profile(models.Model):
    username=models.OneToOneField(User,on_delete=models.CASCADE)
    adress=models.TextField()
    profile_pic=models.ImageField()

    def __str__(self):
        return self.username