from rest_framework import serializers
from api.item_model import ItemModel

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ItemModel
        fields = ('id',
                  'name',
                  'category',
                  'created_at')