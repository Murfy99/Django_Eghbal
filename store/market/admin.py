from django.contrib import admin
from . import models
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    readonly_fields = ('uuid',)
    list_display = ('name','price','count','category')
    list_filter = ('price',)
    search_fields = ('name','price',)
class CategoryAdmin(admin.ModelAdmin):
    ... 

admin.site.register(models.Product, ProductAdmin)
admin.site.register(models.Category, CategoryAdmin)