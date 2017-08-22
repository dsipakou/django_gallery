from rest_framework import serializers

from app.models import Image


class ImageSerializer(serializers.ModelSerializer):
    image = serializers.SerializerMethodField('serialize_image')

    class Meta:
        model = Image
        fields = ('id', 'name', 'desc', 'image', 'created_at', 'updated_at')

    def serialize_image(self, image):
        return image.image.url if image else None
