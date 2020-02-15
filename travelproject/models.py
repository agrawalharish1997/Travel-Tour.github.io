# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
cat='categorised'
uncat='uncategorised'
options = (
(cat, 'categorised'),
(uncat, 'uncategorised')
)


# Create your models here.
class Hotel(models.Model):
    country=models.CharField(max_length=100)
    place=models.CharField(max_length=100)
    name=models.CharField(max_length=100) 
    price=models.IntegerField(default =0)
    img=models.ImageField(upload_to='pics/hotel')

    def __str__(self):
        return self.text


class Tour(models.Model):
    img=models.ImageField(upload_to='pics/tour')
    price=models.IntegerField(default =0)
    datefrom=models.DateField()
    dateto=models.DateField()
    country=models.CharField(max_length=100)

    

class BestRoom(models.Model):
    img=models.ImageField(upload_to='pics/room')
    price=models.IntegerField(default=0)
    name=models.CharField(max_length=100) 
    pernight=models.BooleanField(default=True)


class InstagramGallery(models.Model):
    img=models.ImageField(upload_to='pics/InstagramGallery')


class LatestPost(models.Model):
    img=models.ImageField(upload_to='pics/LatestPost')
    title=models.CharField(max_length=100) 
    date=models.DateField()
    name=models.CharField(max_length=100) 




class Blog(models.Model):
    img=models.ImageField(upload_to='pics/blog')
    name=models.CharField(max_length=100) 
    desc=models.TextField()
    date=models.DateField()
    categoties=models.CharField(choices=options,max_length=100,default='uncategorised') 

   
    #Slug=models.SlugField(max_length=200,unique=True)

    

class Comment(models.Model):
    post_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)



class User1(models.Model):
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100) 
    username=models.EmailField(max_length=254)
    password=models.CharField(max_length=100) 

    