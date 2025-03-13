from rest_framework import serializers
from drink.models import Drink

class DrinkSerializer (serializers.ModelSerializer):
    class Meta:
        model = Drink
        fields = ('id', 'name', 'price', 'description', 'created_at', 'updated_at')