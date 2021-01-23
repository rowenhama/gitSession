from django.db import models

# Create your models here.
class Registration(models.Model):
    username = models.CharField(max_length=50)
    fullname = models.CharField(max_length=50)
    date_of_birth = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=50)