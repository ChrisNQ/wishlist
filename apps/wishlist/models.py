from __future__ import unicode_literals
from ..loginreg.models import User
from django.db import models

# Create your models here.
class ProductManager(models.Manager):
    def validateproduct(self, data, user_id):
        errors = []
        if len(data["addedproduct"]) < 2:
            errors.append("Please enter a product for your wishlist")
            return(False, errors)
        else:
            Product.objects.create(users=User.objects.get(id=user_id), productname=data["addedproduct"])
            return(True, data)


class Product(models.Model):
    productname = models.CharField(max_length = 30)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    wishlist_item = models.ManyToManyField(User, related_name = "ManyUsers")
    users = models.ForeignKey(User)
    objects = ProductManager()
