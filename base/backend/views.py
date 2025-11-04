from django.shortcuts import render # type: ignore
from rest_framework.decorators import api_view # type: ignore
from rest_framework.response import Response # type: ignore
from rest_framework import status # type: ignore
from .models import normal_user, vendor_admin, Product
from .serializer import normal_userSerializer, vendor_adminSerializer, ProductSerializer

# Create your views here.
@api_view(['GET'])
def get_vendor_admin(request):
    v_adm_obj = vendor_admin.objects.all()
    serializedObj = vendor_adminSerializer(v_adm_obj, many=True).data
    return Response(serializedObj)

@api_view(['GET'])
def get_normal_user(request):
    normal_user_obj = normal_user.objects.all()
    serializedObj = normal_userSerializer(normal_user_obj, many=True).data
    return Response(serializedObj)

