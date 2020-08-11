from django.contrib import admin

from .models import ProductInformation, ProductCategory, ProductSubcategory, User

admin.site.register(ProductInformation)
admin.site.register(ProductCategory)
admin.site.register(ProductSubcategory)
