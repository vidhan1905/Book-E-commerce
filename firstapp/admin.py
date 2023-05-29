from django.contrib import admin
from firstapp.models import *
# Register your models here.
admin.site.register(Category)

class productregister(admin.ModelAdmin):
    list_display=['name','price','description']

admin.site.register(Product,productregister)


class userregister(admin.ModelAdmin):
    list_display=['name','email','phone']

admin.site.register(UserRegister,userregister)

class contactregister(admin.ModelAdmin):
    list_display=['name','email','phone']
admin.site.register(Contact,contactregister)

class orderresigter(admin.ModelAdmin):
    list_display=['userName','userEmail']
admin.site.register(Ordermodel,orderresigter)