from rest_framework.serializers import Serializer
from rest_framework.serializers import ModelSerializer
from . import models

class ProductSerializer(ModelSerializer):
    class Meta:
        model = models.Product
        fields = '__all__'