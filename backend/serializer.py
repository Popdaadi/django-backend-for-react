from rest_framework import serializers  # type: ignore
from .models import normal_user, vendor_admin, Product, Product_images

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class vendor_adminSerializer(serializers.ModelSerializer):
    class Meta:
        model = vendor_admin
        fields = '__all__'

    
    def get_img_url(self, obj):
        request = self.context.get('request')
        img_url = obj.fingerprint.url
        return request.build_absolute_uri(img_url)
       

class product_imagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product_images
        fields = '__all__'

    def get_img_url(self, obj):
        request = self.context.get('request')
        img_url = obj.fingerprint.url
        return request.build_absolute_uri(img_url)
       


class normal_userSerializer(serializers.ModelSerializer):
    class Meta:
        model = normal_user
        fields = '__all__'
       