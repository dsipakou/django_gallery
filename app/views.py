from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Image
from app.serializers import ImageSerializer


class ImagesView(APIView):
    authentication_classes = ()
    permission_classes = ()

    model = Image
    serializer_class = ImageSerializer

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

class ImageView(APIView):
    authentication_classes = ()
    permission_classes = ()
    model = Image
    serializer_class = ImageSerializer

    def get(self, request, image_id):
        image = Image.objects.get(id=image_id)
        serializer = ImageSerializer(image, many=False)
        return Response(serializer.data)

