#from django.shortcuts import render
#from django.http import HttpResponse
from app.models import Post
from django.contrib.auth.models import User

from api.serializers import PostSerializer, RegSerializer #. for same directory
from rest_framework import status,permissions
from rest_framework.decorators import api_view,permission_classes
#from rest_framework.views import APIView# for class name(APiVew) else you have to use decorator
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token
"""" this function will create  tokens for already registered users"""
# from django.contrib.auth.models import User

# for user in User.objects.all():
#     Token.objects.get_or_create(user=user)
#=====================================================================



@api_view(['GET', 'POST']) #The renderer instance that will be used to render the response
@permission_classes([IsAuthenticated]) #can't access without token
def list_post(request):
    if request.method == 'GET':
        print(request.data)
        posts=Post.objects.all()
        post_serializer=PostSerializer(posts, many=True)
        return Response(post_serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def detail_post(request,post):
    try:
        posts=Post.objects.get(pk=post)#id=post
    except Post.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PostSerializer(posts)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PostSerializer(posts, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        posts.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def registeruser(request):
    if request.method == 'POST':
        serializer = RegSerializer(data=request.data)
        print(serializer.is_valid())
        data={}
        if serializer.is_valid():
            user = serializer.save() #new user
            token = Token.objects.get(user=user)
            data['username']=user.username
            data['email']=user.email
            data['token']=token.key
            return Response(data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['POST'])
# def loginuser(request):
#     if request.method == 'POST':
#         serializer = LoginSerializer(data=request.data)
#         print(serializer.is_valid())
#         data={}
#         if serializer.is_valid():
#             user = serializer.save() #new user
#             token = Token.objects.get(user=user)
#             data['username']=user.username
#             #data['email']=user.email
#             data['token']=token.key
#             data['Created']=token.created
#             return Response(data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# def index(request):
#     return HttpResponse("<p>hello</p>")

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)


#POST
# {
#     "username":"tester",
#     "password": "1234!@#$",
#      "email":"testtest@test.com"
# }

#RESPONSE
# {
#     "username": "testernew",
#     "email": "testtest@test.com",
#     "token": "3cc6acf4758616207e0092e7a4d3d743b1beae0f"
# }