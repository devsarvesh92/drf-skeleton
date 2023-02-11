from rest_framework.response import Response
from rest_framework.decorators import api_view
from api.serializers import ItemSerizalier
from base.models import Item


@api_view(['GET'])
def get_data(request):
    items = Item.objects.all()
    serializer = ItemSerizalier(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def post_data(request):
    serializer: ItemSerizalier = ItemSerizalier(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)
    


