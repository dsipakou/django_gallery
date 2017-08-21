from rest_framework.response import Response
from rest_framework.views import APIView

from app.models import Image
from app.serializers import ImageSerializer


class ImageView(APIView):
    authentication_classes = ()
    permission_classes = ()

    model = Image
    serializer_class = ImageSerializer

    def get(self, request):
        images = Image.objects.all()
        serializer = ImageSerializer(images, many=True)
        return Response(serializer.data)

