from email import message
from rest_framework.generics import ListAPIView, views
from mainapp import serializers, models
from rest_framework.response import Response
from rest_framework import status
from .services import check_user


class ShopListView(ListAPIView):
    serializer_class = serializers.ShopSerializer
    
    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        return models.Shop.objects.select_related('worker').filter(
            worker__phone=phone
        )
        
        
class VisitShopView(views.APIView):
    def post(self, request, *args, **kwargs):
        phone = request.query_params.get('phone')
        serialized_data = serializers.VisitCreateSerializer(data=request.data)
        if serialized_data.is_valid():
            if not check_user(phone, request.data['id']):
                return Response(
                    'You have no access to this shop', 
                    status=status.HTTP_403_FORBIDDEN
                    )
            visit = serialized_data.save()
            return Response(serializers.VisitSerializer(visit).data)
        return Response(serialized_data.errors ,status=status.HTTP_400_BAD_REQUEST)

 
