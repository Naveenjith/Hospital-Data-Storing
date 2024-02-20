from django.db import models

# Create your models here.
class patient1(models.Model):
    Fname=models.CharField(max_length=60)
    Lname=models.CharField(max_length=60)
    Age=models.IntegerField()
    Adress=models.CharField(max_length=60)
    Email=models.EmailField()
    Disease=models.CharField(max_length=60)