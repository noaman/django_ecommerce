from django.contrib import admin

from shop.models import FulfilmentPartner, Product, ProductApplication, ProductBrand, ProductCategory, ProductSubCategory, Supplier



@admin.register(ProductBrand)
class ProductBrandAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}

@admin.register(ProductApplication)
class ProductApplicationAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}


@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}

@admin.register(ProductSubCategory)
class ProductSubCategoryAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}

@admin.register(FulfilmentPartner)
class FulfilmentPartnerAdmin(admin.ModelAdmin):
    list_display = (['name'])
    prepopulated_fields = {'slug':('name',)}

# admin.site.register(Product)

# # Create your models here.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (['title','brand'])
    list_filter = (['title'])
    search_fields = (['title'])
    prepopulated_fields = {'slug':('title',)}
    # date_hierarchy = 'publish'
    # ordering = ('status', 'publish')