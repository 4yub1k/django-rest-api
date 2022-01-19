from app.models import Post
from rest_framework import serializers

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post #what to show
        fields = ['id','title','content'] #fields to modify