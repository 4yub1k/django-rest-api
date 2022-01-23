from app.models import Post
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import serializers
from rest_framework.validators import UniqueValidator


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post #what to show
        fields = ['id','title','content'] #fields to modify

class RegSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    email = serializers.EmailField(max_length=75, required=True) #modify email filed to importnat
    # password = serializers.CharField()
    #password = serializers.CharField(write_only=True)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']
#class LoginSerializer(serializers.ModelSerializer):
    # username = serializers.CharField()
    #email = serializers.EmailField(max_length=75, required=True) #modify email filed to importnat
    # password = serializers.CharField()
    #password = serializers.CharField(write_only=True)
