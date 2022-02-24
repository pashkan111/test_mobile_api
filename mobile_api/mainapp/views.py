from email import message
from rest_framework.generics import ListAPIView, views
from mainapp import serializers, models
from rest_framework.response import Response
from rest_framework import status


class ShopListView(ListAPIView):
    serializer_class = serializers.ShopSerializer
    
    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        return models.Shop.objects.select_related('worker').filter(
            worker__phone=phone
        )
        
        
class VisitShopView(views.APIView):
    def post(self, request, *args, **kwargs):
        serialized_data = serializers.VisitCreateSerializer(data=request.data)
        if serialized_data.is_valid():
            visit = serialized_data.save()
            return Response(serializers.VisitSerializer(visit).data)
        return Response(message=serialized_data.error ,status=status.HTTP_400_BAD_REQUEST)

 
