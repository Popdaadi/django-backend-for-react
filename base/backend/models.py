from django.db import models # type: ignore
from django.contrib.auth.models import User  # type: ignore

# Create your models here.
class normal_user(models.Model):
    full_name = models.CharField(help_text="enter your username", max_length=250)
    email_address = models.EmailField(help_text="enter your email",  max_length=250)
    phone_number = models.IntegerField()
    profile_picture = models.ImageField(upload_to='profile_picture',  max_length=250)


class Product(models.Model):
    product_name=models.CharField(help_text="enter yout product name", max_length=100)
    product_price=models.IntegerField()
    product_image = models.ImageField(upload_to='product_image')
    product_category = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.product_name}"


class vendor_admin(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cac_image = models.ImageField(upload_to='cac_document')
    nin_image = models.ImageField(upload_to='nin_document')
    user_profile_pic = models.ImageField(upload_to='user_profile_document')
    full_name = models.CharField(max_length=250)
    business_name = models.CharField( max_length=250)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.business_name}"