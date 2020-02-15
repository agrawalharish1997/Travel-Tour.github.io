from django.conf.urls import url
from . import views
import re as r


urlpatterns = [
    
    url(r'^$',views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    url(r'^login/$',views.login, name='login'),
    url(r'^logout/$',views.logout,name='logout'),
    url(r'^register/$',views.register,name='register'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^offers/$', views.offers, name='offers'),
    url(r'^blog/$',views.blog,name='blog'),
    url(r'^login/register/$',views.register,name='register'),
    url(r'^about/login/$',views.login, name='login'),
    url(r'^about/blog/$',views.blog,name='blog'),
    url(r'^search',views.search,name='serach'),
    url(r'^about/register/$',views.register,name='register'),
    url(r'^about/contact/$',views.contact,name='contact'),
    url(r'^about/offers/$',views.offers,name='offers'),
    url(r'^about/$',views.index,name='index'),
    url(r'^login/login$',views.login,name='login'),
    url(r'^register//$',views.register,name='register'), 
    url(r'^message$',views.Message,name='Message'),
    url(r'^comment/$',views.comment,name='comment'),
    url(r'^blog/comment$',views.comment,name='comment'),
    url(r'^blog/blog$',views.blog,name='blog'),
    url(r'^register/register$',views.register,name='register'),
    url(r'^login/register/register$',views.register,name='register'),
    url(r'^offers/search$',views.search,name='search'),
    url(r'^offers/search/$',views.search,name='search'),
    url(r'^forgetpassword/$',views.forgetpassword,name='forgetpassword'),
  

    
]