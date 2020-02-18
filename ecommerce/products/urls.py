from django.urls import path, include
from django.conf.urls import url
from . views import Home
from django.contrib.flatpages import views as flat_views
app_name= 'mainapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    url(r'^about/$', flat_views.flatpage, {'url': '/about/'}, name='about'),
    url(r'^about_hakuba/$', flat_views.flatpage, {'url': '/about_hakuba/'}, name='abouthakuba'),
    url(r'^faq/$', flat_views.flatpage, {'url': '/faq/'}, name='faq'),
    url(r'^register/$', flat_views.flatpage, {'url': '/register/'}, name='register')
]
