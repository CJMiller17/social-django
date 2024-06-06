from django.contrib import admin
from app_social_media.models import *

class PostInline(admin.TabularInline):
    model = Post
    extra = 1

class ProfileAdmin(admin.ModelAdmin):
    inlines = [PostInline]

class PostAdmin(admin.ModelAdmin):
    list_display = ("profile", "content", "created", "updated")
    search_fields = ("content",)
    list_filter = ("created", "updated", "profile")

class ImageAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile, ProfileAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Image, ImageAdmin)

# Register your models here.
