from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
  user = UserSerializer(read_only = True)
  class Meta:
    model = Profile
    fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
  class Meta:
    model = Image
    fields = '__all__'

class PostSerializer(serializers.ModelSerializer):
  profile = ProfileSerializer(read_only = True)
  image = ImageSerializer(many=True, read_only=True)
  liked_posts = ProfileSerializer( many=True, read_only=True)
  liked_post_count = serializers.IntegerField(source = "liked.count", read_only=True)
  is_liked = serializers.SerializerMethodField() # Look into this field 
  
  class Meta:
    model = Post
    fields = '__all__'

  def get_is_liked(self, obj):
    request = self.context.get("request", None)
    if request:
      return request.user.profile in obj.liked.all()
    return False


class CommentSerializer(serializers.ModelSerializer):
  liked_comments = ProfileSerializer( many=True, read_only=True)
  liked_comment_count = serializers.IntegerField(source = "liked.count", read_only=True)
  is_liked = serializers.SerializerMethodField()
  
  class Meta:
    model = Comment
    fields = '__all__'

  def get_is_liked(self, obj):
    request = self.context.get("request", None)
    if request:
      return request.user.profile in obj.liked.all() 

class LikeSerializer(serializers.ModelSerializer):
  class Meta:
    model = Like
    fields = '__all__'

