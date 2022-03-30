from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=200)
    email=models.EmailField(max_length=100)
    day=models.CharField(max_length=20,null=True,blank=True)
    date=models.DateField(max_length=100,null=True,blank=True)
    doc=models.CharField(max_length=100,null=True,blank=True)
    textarea_message=models.CharField(max_length=1000,null=True,blank=True)
