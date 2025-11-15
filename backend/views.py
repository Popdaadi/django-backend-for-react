from django.shortcuts import render # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from rest_framework.views import APIView # type: ignore
from .models import normal_user, vendor_admin, Product, Product_images
from .serializer import normal_userSerializer, vendor_adminSerializer, ProductSerializer, product_imagesSerializer

# Create your views here.
class productImage(APIView):
    def get(self, request, *args, **kwargs):
        images = Product_images.objects.all()
        serializer = product_imagesSerializer(images, context={'request':request}, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_vendor_admin(request):
    v_adm_obj = vendor_admin.objects.all()
    serializedObj = vendor_adminSerializer(v_adm_obj, context={'request':request}, many=True)
    return Response(serializedObj.data)

@api_view(['GET'])
def get_normal_user(request):
    normal_user_obj = normal_user.objects.all()
    serializedObj = normal_userSerializer(normal_user_obj, many=True).data
    return Response(serializedObj)

