from rest_framework.decorators import parser_classes, api_view, permission_classes
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import *
from .serializers import *


# This is where are the CRUD operations will happen


### PROFILE ###
@api_view(["POST"])
@permission_classes([])
def create_profile(request):
    print("create profile request: ", request)
    user = User.objects.create(username = request.data["username"])
    user.set_password(request.data["password"])
    user.save()

    profile = Profile.objects.create(
        user = user,
        first_name = request.data["first_name"], # Why do we use brackets?
        last_name = request.data["last_name"]
    )
    profile.save()
    serialized_profile = ProfileSerializer(profile)
    print("profile created: ", serialized_profile.data)
    return Response(serialized_profile.data)


@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_profile(request):
    print("get profile request: ", request)
    serialized_profile = ProfileSerializer(request.user.profile)
    return Response(serialized_profile.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_profile(request):
    print("Updated Profile")


@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_profile(request, pk):
    profile = get_object_or_404(Profile, pk = pk)
    profile.delete()
    print("Deleted Profile")
    return Response(status = status.HTTP_204_NO_CONTENT)


### POST ###
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_post(request):
    profile = Profile.objects.get(user = request.user)
    post = Post.objects.create(
        content = request.data["content"],
        profile = profile,
        # images =  # How does view handle 1-many inputs? Does profile need to be added?
    )
    serialized_post = PostSerializer(post) # User has to be attached and images as well
    print("Created post")
    return Response(serialized_post.data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_post(request):
    print("Read post", request)
    posts = Post.objects.all().order_by("-created")
    serialized_post = PostSerializer(posts, many = True)
    return Response(serialized_post.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_post(request):
    print("Updated post")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_post(request, pk):
    post = get_object_or_404(Post, pk = pk)
    post.delete()
    print("Deleted post")
    return Response(status = status.HTTP_204_NO_CONTENT)   



### COMMENTS ###
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_comment(request):
    comment = Comment.objects.create(
        content = request.data["content"] # How does view handle 1-many inputs? Does profile need to be added?
    )
    serialized_comment = CommentSerializer(comment)
    print("Created comment")
    return Response(serialized_comment.data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_comment(request):
    print("Read comment", request)
    comments = Comment.objects.all()
    serialized_comment = CommentSerializer(comments, many =True)
    return Response(serialized_comment.data)

@api_view(["PUT"])
@permission_classes([IsAuthenticated])
def update_comment(request):
    print("Updated comment")

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk = pk)
    comment.delete()
    print("Deleted comment")
    return Response(status = status.HTTP_204_NO_CONTENT)



### LIKES ###
@api_view(["POST"])
@permission_classes([IsAuthenticated])
def create_like(request):
    post_like = "post_id" in request.data
    comment_like = "comment_id" in request.data

    if post_like:
        post_id = request.data["post_id"]
        post = get_object_or_404(Post, pk = post_id)
        like = Like.objects.create(post = post)
        print("created post like")
    elif comment_like:
        comment_id = request.data["comment_id"]
        comment = get_object_or_404(Comment, pk = comment_id)
        like = Like.objects.create(comment = comment)
        print("created comment like")
    else:
        return Response(status = status.HTTP_400_BAD_REQUEST)
    serialized_like = LikeSerializer(like)
    return Response(serialized_like.data)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_like(request):
    print("Read like", request)
    likes = Like.objects.all()
    serialized_like = LikeSerializer(likes, many = True)
    return Response(serialized_like.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_like(request, pk):
    like = get_object_or_404(Like, pk = pk)
    like.delete()
    print("Deleted like")
    return Response(status = status.HTTP_204_NO_CONTENT)
    



### IMAGES ###
@api_view(["POST"])
@permission_classes([IsAuthenticated])
@parser_classes([MultiPartParser, FormParser])
def create_image(request):
    serialized_image = ImageSerializer(data = request.data)
    if serialized_image.is_valid():
        serialized_image.save()
        print("Created image")
        return Response(serialized_image.data, status = status.HTTP_201_CREATED)
    return Response(serialized_image.errors, status = status.HTTP_400_BAD_REQUEST)
    

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def get_image(request):
    print("Read image", request)
    images = Image.objects.all()
    serialized_image = ImageSerializer(images, many = True)
    return Response(serialized_image.data)

@api_view(["DELETE"])
@permission_classes([IsAuthenticated])
def delete_image(request, pk):
    image = get_object_or_404(Image, pk = pk)
    image.delete()
    print("Deleted image")
    return Response(status = status.HTTP_204_NO_CONTENT)