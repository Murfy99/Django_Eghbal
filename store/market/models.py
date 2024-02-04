from django.db import models
import uuid

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length = 255)
    price = models.PositiveIntegerField()
    count = models.PositiveIntegerField()
    description = models.TextField()
    create_date = models.DateTimeField(auto_now_add = True)
    last_edit_date = models.DateTimeField(auto_now = True)
    uuid = models.UUIDField(default = uuid.uuid4, primary_key=True)
    # discount = models.DecimalField(decimal_places=3)
    category = models.ForeignKey('Category', on_delete=models.PROTECT)

    
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
    # null , blank baraye inke majbor nabashim hame parent dashte bashan
# class Tag(models.Model):
    # product = models.ManyToManyRel(Product, on_delete=models.CASCADE)
#     tag_name = models.CharField(max_length = 25)