from django.urls import path
from firstapp.views import *

urlpatterns = [
    path('first',first),
    path('login/',login1,name='login1'),
    path('logout/',logout,name='logout'),
    path('table/',table_view),
    path('table_filter/',table_filter),
    path('table_get/',table_getdata),
    path("",index,name='index'),
    path('about-us/',about,name='aboutus'),
    path('productall/',productall,name='productall'),
    path('productfilter/<int:id>/',productcategorywise,name='productfilter1'),
    path('productget/<int:id>/',singleproduct,name='productget1'),
    path('register',register,name='register1'),
    path('contact',contact,name='contactus'),
    path('changepass/',changepass,name='changepassword'),
    path('changeprof/',changeprofile,name='change'),
    path('buy-now',buynow,name='buy'),
    path('razorpayView/',razorpayView,name='razorpayview'),
    path('paymenthandler/',paymenthandler,name='paymenthandler'),
    path('order-success/',successview,name='orderSuccessView'),
    path('myorders/',myorder,name='myorder')
] 
