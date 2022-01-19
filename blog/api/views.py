#from django.shortcuts import render
#from django.http import HttpResponse
from app.models import Post
from .serializers import PostSerializer #. for same directory
from rest_framework import status,permissions
from rest_framework.decorators import api_view
#from rest_framework.views import APIView# for class name(APiVew) else you have to use decorator
from rest_framework.response import Response

@api_view(['GET', 'POST']) #The renderer instance that will be used to render the response
def list_post(request):
    if request.method == 'GET':
        posts=Post.objects.all()
        post_serializer=PostSerializer(posts, many=True)
        return Response(post_serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# def index(request):
#     return HttpResponse("<p>hello</p>")