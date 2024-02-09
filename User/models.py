from django.db import models

# Create your models here.
class Slider1Model(models.Model):
   slider_image = models.ImageField(upload_to='static/uploads')
   slider_titel=models.CharField(max_length=50)
   slider_btn=models.CharField(max_length=50)
   slider_description=models.CharField(max_length=100)
   slider_link=models.CharField(max_length=200)
   
   def __str__(self):
      return self.slider_titel
# Brand Model
class BrandModel(models.Model):
   brand_name=models.CharField(max_length=200)
   brand_des=models.CharField(max_length=200)
   brand_logo=models.ImageField(upload_to='static/logo')
   def __str__(self):
      return self.brand_name

# Category Model
class CategoryModel(models.Model):
   category_name=models.CharField(max_length=200)
   categoty_des=models.TextField()
   category_logo=models.ImageField(upload_to='static/logo')
   def __str__(self):
      return self.category_name
   

#Product Model
class ProductModel(models.Model):
   product_img = models.ImageField(upload_to='static/uploads' , default='' ,null=True)
   product_name=models.CharField(max_length=200)
   brand=models.ForeignKey(BrandModel,on_delete=models.CASCADE)
   product_price=models.IntegerField()
   product_dis=models.TextField()
   product_Warranty=models.CharField(max_length=200)
   category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
   product_color=models.CharField(max_length=300)
   def __str__(self):
      return self.product_name
# user
class UserModel(models.Model):
   user_name = models.CharField(max_length=100)
   user_mobile=models.CharField(max_length=30)
   user_address=models.TextField()
   user_email=models.CharField(max_length=100)
   user_password=models.CharField(max_length=100)
   def __str__(self):
      return self.user_name
# why choose as page
class WhychooseusModel(models.Model):
   whychooseus_logo=models.FileField(upload_to='static/logo')
   whychooseus_titel=models.TextField(max_length=100)
   whychooseus_dis=models.TextField()
   def __str__(self):
      return self.whychooseus_titel
#upcomming slider 
class UpcommingModel(models.Model):
   upcomming_name=models.CharField(max_length=200,default='' ,null=True)
   upcomming_image=models.ImageField(upload_to='static/uploads')
   category=models.ForeignKey(CategoryModel,on_delete=models.CASCADE)
   def __str__(self):
      return self.upcomming_name


   
    
  