from django.db import models
import uuid
from django.utils import timezone
import os
# from account.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


def _get_file_name(obj,file):
    name = uuid.uuid4()
    ext = os.path.splitext(file)[1].lower()
    path = timezone.now().strftime("product_images/%Y/%m/%d")
    return os.path.join(path,f'{name}{ext}')

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    description = models.TextField(null=True)
    create_date = models.DateTimeField(auto_now_add = True)
    last_edit_date = models.DateTimeField(auto_now = True)
    uuid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    # discount = models.DecimalField(decimal_places=3)
    # enable = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)
    image = models.ImageField(upload_to=_get_file_name, null=True, blank=True)


    def __str__(self) -> str:
        return self.name

# class Comment(models.Model):
#     product = models.ForeignKey(Product, on_delete=models.CASCADE)
#     text = models.TextField()

# class Rank(models.Model):
#     product = models.OneToOneField(Product, on_delete=models.CASCADE)
#     rank = models.PositiveIntegerField()
class Category(models.Model):
    category_name = models.CharField(max_length = 25)
    parent = models.ForeignKey('Category', on_delete=models.CASCADE,
                               null = True, blank = True)
    def __str__(self) -> str:
        return self.category_name
    # null , blank baraye inke majbor nabashim hame parent dashte bashan
# class Tag(models.Model):
    # product = models.ManyToManyRel(Product, on_delete=models.CASCADE)
#     tag_name = models.CharField(max_length = 25)
    
from market.models import *
objects =[]
cat = Category.objects.last()
for i in range(100):
    objects.append(Product(name=f"p_{i}",price=i*10,count=i+5,category=cat))
Product.objects.bulk_create(objects)


class Comment(models.Model):
    user = models.ForeignKey(User,related_name='comments',
                                on_delete = models.PROTECT)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    is_published = models.BooleanField(default = False)
    product = models.ForeignKey('Product',related_name='comments',
                                on_delete = models.CASCADE)
