from rest_framework import serializers

from boards.models import BoardImage, Board


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = "__all__"


class BoardImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = BoardImage
        fields = "__all__"
