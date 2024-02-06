from django.contrib import admin
from . import models
# Register your models here.

class AdminUser(admin.ModelAdmin):
    ...

admin.site.register(models.User, AdminUser )