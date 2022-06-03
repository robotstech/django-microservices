from rest_framework.viewsets import ModelViewSet

from boards.models import Board, BoardImage
from boards.serializers import BoardSerializer, BoardImageSerializer


class BoardViewSet(ModelViewSet):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer


class BoardImageViewSet(ModelViewSet):
    queryset = BoardImage.objects.all()
    serializer_class = BoardImageSerializer
