from django.db import models

# Create your models here.
class doctor1(models.Model):
    Fname=models.CharField(max_length=60)
    Lname=models.CharField(max_length=60)
    Age=models.IntegerField()
    Adress=models.CharField(max_length=60)
    Email=models.EmailField()
    Experiance=models.IntegerField()