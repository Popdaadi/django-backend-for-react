from django.urls import path # type: ignore
from .views import get_vendor_admin, get_normal_user, productImage


urlpatterns = [
    path('vendors/', get_vendor_admin, name='get_vendor_admin'),
    path('users/', get_normal_user, name='get_normal_user'),
    path('product-image/', productImage.as_view(), ),
]

