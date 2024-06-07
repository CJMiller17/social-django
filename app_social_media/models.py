from django.db import models
from django.contrib.auth.models import User


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile")
    avatar = models.ImageField(upload_to="image/", null=True, blank=True)
    first_name = models.TextField()
    last_name = models.TextField()
    title = models.TextField(null=True, blank=True)
    creation_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Post(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.ManyToManyField(Profile, blank=True, related_name="post_liked")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    
    def liked_posts(self):
        return self.liked.all()

class Comment(models.Model):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    content = models.TextField()
    liked = models.ManyToManyField(Profile, blank=True, related_name="comment_liked")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def liked_comments(self):
        return self.liked.all()

STATUS = (
    ("like", "like"),
    ("unlike", "unlike")
)

class Like(models.Model):
    profile = models.ManyToManyField(Profile)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True)
    status = models.CharField(choices=STATUS, default="like", max_length=10)


class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="image")
    created = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    image = models.ImageField(upload_to="images/", null=True, blank=True)