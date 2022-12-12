from django.contrib import admin

# Register your models here.

# 將個 database 放入 admin 度
from .models import Listing

admin.site.register(Listing)