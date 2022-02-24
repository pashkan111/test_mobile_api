from rest_framework import serializers
from . import models


class ShopSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Shop
        fields = ('id', 'name')


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Visit
        fields = ('id', 'date')
        

class VisitCreateSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    latitude = serializers.FloatField()
    longitude = serializers.FloatField()
        
    def create(self, validated_data):
        shop_id = validated_data.pop('id')
        shop = models.Shop.objects.filter(id=shop_id).first()
        new_visit = models.Visit.objects.create(
            shop=shop,
            **validated_data
        )
        return new_visit
    