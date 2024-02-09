from django.utils.html import format_html
from asyncio import format_helpers
from django.contrib import admin

from .models import BrandModel, CategoryModel, ProductModel, Slider1Model,WhychooseusModel,UpcommingModel

# Register your models here.
class SliderAdmin(admin.ModelAdmin):
   list_display=['slider_titel','slider_btn','display_image']
   def display_image(self,obj):
      return format_html('<img src="{}" width="100" heigth="100"/>',obj.slider_image.url)
   display_image.short_description='slider_image'
admin.site.register(Slider1Model,SliderAdmin)

class BrandAdmin(admin.ModelAdmin):
   list_display=['brand_name','brand_des','display_image']
   def display_image(self,obj):
      return format_html('<img src="{}" width="200" heigth="200"/>',obj.brand_logo.url)
   display_image.short_description='brand_logo'
admin.site.register(BrandModel,BrandAdmin)

class CategoryAdmin(admin.ModelAdmin):
   list_display=['category_name','categoty_des','display_image']
   def display_image(self,obj):
      return format_html('<img src="{}" width="200" heigth="200"/>',obj.category_logo.url)
   display_image.short_description='category_logo'
admin.site.register(CategoryModel,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
   list_display=['product_name','brand','product_price','product_Warranty','category','display_image']
   def display_image(self,obj):
      return format_html('<img src="{}" width="100" heigth="100"/>',obj.product_img.url)
   display_image.short_description='product_img'
admin.site.register(ProductModel,ProductAdmin)

class WhychooseusAdmin(admin.ModelAdmin):
   list_display=['whychooseus_titel','whychooseus_dis','display_image']
   def display_image(self,obj):
      return format_html('<img src="{}" width="100" heigth="100"/>',obj.whychooseus_logo.url)
   display_image.short_description='logo'
admin.site.register(WhychooseusModel,WhychooseusAdmin)

class UpcommingAdmin(admin.ModelAdmin):
   list_display=['display_image','category']
   def display_image(self,obj):
      return format_html('<img src="{}" width="70%" heigth="100"/>',obj.upcomming_image.url)
   display_image.short_description='image'
admin.site.register(UpcommingModel,UpcommingAdmin)
