"""message_board_comments URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from comments.views import CommentImageViewSet, CommentViewSet
from message_board_comments import settings
from message_board_comments.settings import API_PREFIX

router = DefaultRouter()
router.register("comments", CommentViewSet, basename="comments")
router.register("comment-images", CommentImageViewSet, basename="comment-images")

urlpatterns = [
    path('admin/', admin.site.urls),

    # apps
    path(f'{API_PREFIX}/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
