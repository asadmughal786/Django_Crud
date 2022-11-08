from django.db import models

# Create your models here.

class App_Users(models.Model):
    First_Name = models.CharField(max_length = 30)
    Last_name = models.CharField(max_length = 30)
    email = models.EmailField(max_length = 20)
    password = models.CharField(max_length = 30)
    confirm_Password = models.CharField(max_length = 30)