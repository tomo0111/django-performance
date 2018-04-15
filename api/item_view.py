from rest_framework.response import Response
from rest_framework.views import APIView

from api.item_model import ItemModel
from api.item_serializer import ItemSerializer

class ItemView(APIView):

    def get(self, request):
        snippets = ItemModel.objects.all()
        serializer = ItemSerializer(snippets, many=True)
        return Response(serializer.data)
