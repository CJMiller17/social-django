"""
URL configuration for proj_social_media project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from rest_framework import routers
from app_social_media.views import *
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView
)

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("token/", TokenObtainPairView.as_view(), name = "token_obtain_pair"),
    path("refresh/", TokenRefreshView.as_view(), name = "token_refresh"),

    # PROFILES
    path("profile/create/", create_profile, name = "create_profile"),
    path("profile/", get_profile, name = "get_profile"),
    path("profile/update/", update_profile, name = "update_profile"),
    path("profile/delete/<int:pk>", delete_profile, name = "delete_profile"),

    # POSTS
    path("post/create/", create_post, name = "create_post"),
    path("post/", get_post, name = "get_profile"),
    path("post/update/", update_post, name = "update_post"),
    path("post/delete/<int:pk>", delete_post, name = "delete_post"),

    # COMMENTS
    path("comment/create/", create_comment, name = "create_comment"),
    path("comment/", get_comment, name = "get_comment"),
    path("comment/update/", update_comment, name = "update_comment"),
    path("comment/delete/<int:pk>", delete_comment, name = "delete_comment"),

    # LIKES
    path("like/create/", create_like, name = "create_like"),
    path("like/", get_like, name = "get_like"),
    path("like/delete/<int:pk>", delete_like, name = "delete_like"),
    
    # IMAGES
    path("image/create/", create_image, name = "create_image"),
    path("image/", get_image, name = "get_image"),
    path("image/delete/<int:pk>", delete_image, name = "delete_image"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)