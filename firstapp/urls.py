from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('first',first),
    path('login/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('vendorlogin/',vendorlogin1,name='login2'),
    path('vendorlogout/',vendorlogout,name='logout1'),
    path("",index,name='index'),
    path('about-us/',about,name='aboutus'),
    path('productall/',productall,name='productall'),
    path('productfilter/<int:id>/',productcategorywise,name='productfilter1'),
    path('productget/<int:id>/',singleproduct,name='productget1'),
    path('register',register,name='register1'),
    path('vendorregister',vendorregister,name='vendor_register'),
    path('contact',contact,name='contactus'),
    path('changepass/',changepass,name='changepassword'),
    path('forget-password/',forget,name='forget'),
    path('changeprof/',changeprofile,name='change'),
    path('buy-now',buynow,name='buy'),
    path('razorpayView/',razorpayView,name='razorpayview'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-success/',successview,name='orderSuccessView'),
    path('myorders/',myorder,name='myorder'),
    path('search/',searchview,name='search'),
    path('addproduct',addproduct,name='addproduct')
] 
