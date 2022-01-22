from rest_framework.viewsets import ModelViewSet

from comments.models import Comment, CommentImage
from comments.serializers import CommentSerializer, CommentImageSerializer


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer


class CommentImageViewSet(ModelViewSet):
    queryset = CommentImage.objects.all()
    serializer_class = CommentImageSerializer
