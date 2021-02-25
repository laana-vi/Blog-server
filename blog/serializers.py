from rest_framework import serializers
from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'author', 'content', 'status', 'timestamp', 'likes', 'category', 'slug', 'image')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields=('id', "name")