# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
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
class Car(models.Model):
    img=models.ImageField(upload_to='pics/car')
    destination1=models.CharField(max_length=100,default='india')
    carNo=models.CharField(max_length=100)
    source1=models.CharField(max_length=100)
    name=models.CharField(max_length=100)
    noseat=models.IntegerField(default=0)
    price=models.IntegerField(default=0)
    review=models.CharField(max_length=100 ,default='Very Good')
    desc=models.TextField(default='Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vivamus quis vu lputate eros, iaculis consequat nisl. Nunc et suscipit urna. Integer eleme ntum orci eu vehicula pretium.')

    
class SMS(models.Model):
    name=models.CharField(max_length=100) 
    email=models.EmailField()
    subject=models.CharField(max_length=200)
    message=models.TextField()





from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
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
    #post_id=models.ForeignKey(Blog,on_delete=models.CASCADE)
    #user_id=models.ForeignKey(User,on_delete=models.CASCADE)
    body=models.TextField()
    comment_date=models.DateTimeField(auto_now_add=True)



class User1(models.Model):
    first_name=models.CharField(max_length=100) 
    last_name=models.CharField(max_length=100) 
    username=models.EmailField(max_length=254)
    password=models.CharField(max_length=100) 

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100, blank=True)
    last_name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=150)
    bio = models.TextField()

    def __str__(self):
        return self.user.username

@receiver(post_save, sender=User)
def update_profile_signal(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()