from django.http import HttpResponse
from django.shortcuts import redirect, render
from User.models import CategoryModel, Slider1Model,ProductModel, UpcommingModel,UserModel, WhychooseusModel

# Create your views here.
#login
def login(req):
   return render(req,'login.html')
# register page 
def register(req):
   return render(req,'register.html')
#save user
def save_user(req):
   user=UserModel()
   user.user_name=req.POST['user_name']
   user.user_mobile=req.POST['user_mobile']
   user.user_address=req.POST['user_address']
   user.user_email=req.POST['user_email']
   user.user_password=req.POST['user_password']
   user.save()
   return redirect('/login')
#Check login /session
def check_login(req):
   login_data=UserModel.objects.filter(user_email=req.POST['user_email'],
                                    user_password=req.POST['user_password'],)
   if (len(login_data)>0):
      req.session['user_id']=login_data[0].id
      return redirect('/')
   else:
      return HttpResponse("<script>location.href='/register';</script>")
   
# index page main page
def index(req):
   slider=Slider1Model.objects.all()
   product=ProductModel.objects.all()[:4]
   whychooseus=WhychooseusModel.objects.all()
   category=CategoryModel.objects.all()[:6]
   upcoming=UpcommingModel.objects.all()
   phone=ProductModel.objects.filter(category__category_name='phone') [:6]
   fashion=ProductModel.objects.filter(category__category_name='Fashion') [:6]

   obj={'slider':slider,'product':product,'whychooseus':whychooseus,'category':category,'upcoming':upcoming,'phone':phone,
        'fashion':fashion}
   return render(req,'index.html',obj) 

def add_to_cart(req):
   product1=ProductModel.objects.filter(product_Warranty='2 ',brand__brand_name='Samsung') 
   return render(req,'productinfo.html')
def product_info(req):
   product=ProductModel.objects.filter(id=req.GET['id']); 
   obj={'product':product}
   return render(req,'productinfo.html',obj)