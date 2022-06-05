from django.contrib import admin

# Register your models here.
from .models import Brand
class BrandAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    list_filter =["name","name",]

    class Meta:
        model = Brand

admin.site.register(Brand,BrandAdmin)

from .models import Category
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name",]
    search_fields = ["name",]
    list_filter =["name","name",]

    class Meta:
        model = Category
admin.site.register(Category, CategoryAdmin)

from .models import Product
class ProductAdmin(admin.ModelAdmin):
    list_display = ["name", "price", "brand", "category",]
    search_fields = ["name", "price", "brand__name", "category__name",]
    list_filter = ["brand","category",]
    readonly_fields = []

    class Meta:
        model  = Product
admin.site.register(Product, ProductAdmin)
