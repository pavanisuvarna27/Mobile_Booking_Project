from django.contrib import admin
from .models import product,category,Order
#from .models.admin import Admin


class AdminProduct(admin.ModelAdmin):
    list_display = ['id','name', 'price', 'category']



class AdminCategory(admin.ModelAdmin):
    list_display = ['name']


# Register your models here.
admin.site.register(product, AdminProduct)
admin.site.register(category , AdminCategory)
admin.site.register(Order )
