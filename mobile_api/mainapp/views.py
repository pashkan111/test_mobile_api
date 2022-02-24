from rest_framework.generics import ListAPIView
from mainapp import serializers, models


class ShopListView(ListAPIView):
    serializer_class = serializers.ShopSerializer
    
    def get_queryset(self):
        phone = self.request.query_params.get('phone')
        return models.Shop.objects.select_related('worker').filter(
            worker__phone=phone
        )