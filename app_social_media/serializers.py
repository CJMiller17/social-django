from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profile
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Post
    fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
  class Meta:
    model = Comment
    fields = '__all__'

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = '__all__'