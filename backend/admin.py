from django.contrib import admin # type: ignore
from . models import normal_user, vendor_admin, Product, Product_images

# Register your models here.
admin.site.register(normal_user)
admin.site.register(vendor_admin)
admin.site.register(Product)
admin.site.register(Product_images)
