from django.db import models

# Create your models here.


class ContactUs(models.Model):
    Name = models.CharField(max_length=20)
    Age = models.IntegerField()
    Email = models.CharField(max_length=100)
    Messgae = models.TextField()