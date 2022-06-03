from rest_framework.viewsets import ModelViewSet

from images.models import Image
from images.serializers import ImageSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
