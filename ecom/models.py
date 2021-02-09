from django.db import models

# Create your models here
class Ids(models.Model):
    email=models.CharField(max_length=122)
    password=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    address2=models.CharField(max_length=122)
    city=models.CharField(max_length=122)