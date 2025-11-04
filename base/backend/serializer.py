from rest_framework import serializers  # type: ignore
from .models import normal_user, vendor_admin, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class vendor_adminSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_admin
        fields = '__all__'


class normal_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = normal_user
        fields = '__all__'
       