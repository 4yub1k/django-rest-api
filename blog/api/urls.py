from django.urls import path
from . import views

urlpatterns = [
    #if you have created class in views then
    #path('',views.list_post.as_view(), name='list_post')
    path('',views.list_post, name='list_post'),
    #path('',views.index, name='index')
]