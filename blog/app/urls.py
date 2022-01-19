from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('about',views.about, name='about'),
    path('p/<int:post>',views.post_, name='p'), #html in users post_.html
    path('add/',views.add, name='add') #html in users addpost.html
]