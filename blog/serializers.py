from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import Post, Comment


class PostListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        field = ['id', 'title', 'image', 'like', 'category']