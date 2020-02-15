# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.conf import settings
from django.shortcuts import render,redirect
from offers.models import Hotel
from offers.models import Tour
from offers.models import BestRoom
from offers.models import LatestPost
from offers.models import Blog
from offers.models import User1
from offers.models import InstagramGallery
from offers.models import Comment
from message.models import Sms
from message.models import Room
from offers.models import Car
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django import forms
from django.contrib.auth import login, authenticate
from offers.forms import SignUpForm
from django.contrib.auth.forms import UserCreationForm
 

# Create your views here.
def index(request):
    tour=Tour.objects.all()
    hotel=Hotel.objects.all()
    room=BestRoom.objects.all()
    return  render(request,'index.html',{'room':room, 'hotel':hotel, 'tour':tour})
def about(request):
    return  render(request,'about.html')

def login(request):
    if request.method=='POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            raw_password==make_password(raw_password)
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('/')
        else: 
            messages.info(request,'invalid email or password')
            return redirect('login')
    

    return render(request,'login.html')
        #username1=request.POST.get('username')
        #password1=request.POST.get('Password')
    '''username1=request.POST['username']
        password=request.POST['password']
        hashed_pwd1=make_password(password)
        # user=authenticate(username=username1,password=hashed_pwd1)    
        user=auth.authenticate(request,username="username1",password="hashed_pwd1")       
        #user.save()
        if user is not None: 
        auth.login(request,user, backend='django.contrib.auth.backends.ModelBackend')
        messages.info(request,"login is successfully done !!!")
        return redirect('/') '''      
       
    

    #return render(request,'login.html')
def logout(request):
        auth.logout(request)
        return redirect('/')
def forgetpassword(request):
    pass
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email'] 
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            hashed_pwd = make_password(password1)
            if User.objects.filter(username=username).exists():
                messages.info(request,'email already used ! Try with different Email ')
                return redirect('register')
            else: 
                user=User.objects.create_user(password=hashed_pwd,username=username,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.success(request,'User created successfully !!!')
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')
    else: 
        return render(request,'register.html')
    

def contact(request):
    return render(request,'contact.html' )

def blog(request):
    blog=Blog.objects.all()
    instagramgallery=InstagramGallery.objects.all()
    latestpost=LatestPost.objects.all()
    return render(request,'blog.html',{'blog':blog,'instagramgallery':instagramgallery,'latestpost':latestpost,'comment':comment})
def Message(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        if User.objects.filter(email=email).exists():
        
            msg=Sms.objects.create(name=name,email=email,subject=subject,message=message)
            if msg:
                msg.save()
                messages.success(request,'message is successfully send!!')
                return  redirect('/')
            else:
                redirect("/")
        else:
            messages.info(request,'Your are not login !! login First  ')
            return redirect('register')
    else:
        return render(request,'index.html')
         

def comment(request):
    if request.method=='POST':
        body=request.POST['message']
        blog_id=request.POST['blog_id']
      #  blog=Blog.objects.all() 
        commnt=Comment.objects.create(body=body,post_id=blog_id,date=date.now())
        commnt.save()   
        comment=Comment.objects.all()
    
    else:
        return redirect('blog') 
    return(request,'blog.html',{'comment':comment})
def offers(request):
    oroom=Room.objects.all()
    car=Car.objects.all()
    return render(request,'offers.html',{'oroom':oroom,'car':car})


def search(request):
    destination=request.POST['destination']
    checkin=request.POST['checkin']
    checkout=request.POST['checkout']
    adult=request.POST['adults']
    children=request.POST['children']
    destination1=request.POST['destination1']
    destination3=request.POST['destination3']
    source1=request.POST['source1']
    if destination :
        rooms=Room.objects.filter(Q(place__icontains=destination))
        return render(request,'offers.html',{'rooms':rooms})
    elif destinations1 :
        cars=Car.objects.filter(Q(destination1__icontains=destination1) & Q(source1__icontains=source1))
        return render(request,'offers.html',{'cars':cars}) 
    elif destination3:
        tour=Tour.objects.filters(Q(country__icontains=destination3))
        return render(request,'offers.html',{'tours':tours})
    else:
        messages.info('result Not found !! Search for anaother location')
     





'''

def signup_view(request):
    form = SignUpForm(request.POST)
    if form.is_valid():
        user = form.save()
        user.refresh_from_db()
        user.profile.first_name = form.cleaned_data.get('first_name')
        user.profile.last_name = form.cleaned_data.get('last_name')
        user.profile.email = form.cleaned_data.get('email')
        user.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})'''