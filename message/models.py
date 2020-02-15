# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Sms(models.Model):
    name=models.CharField(max_length=100) 
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()
class Room(models.Model):
    img=models.ImageField(upload_to='pics/Room')
    Name=models.CharField(max_length=100) 
    price=models.IntegerField(default=0)
    Norating=models.CharField(max_length=100) 
    description=models.TextField()
    rating=models.IntegerField(default=0)
    starrating=models.IntegerField(default=0)
    review=models.CharField(max_length=100)
    place=models.CharField(max_length=100 ,default='maldives')