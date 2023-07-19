from django.db.models import Q
import razorpay
from django.core.mail import send_mail
from django.http import HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect
from django.http import HttpResponse
from firstapp.models import *
# Create your views here.


def first(request):
    return HttpResponse("<h1>This is my first web page</h1>")


def login1(request):
    if request.method == "POST":
        emaill = request.POST['email']
        passwordd = request.POST['password']
        try:
            data = UserRegister.objects.get(email=emaill, password=passwordd)
            if data:
                request.session['email'] = data.email
                return redirect('index')
            else:
                return render(request, "login.html", {'message': "Invalid email or password"})
        except:
            return render(request, "login.html", {'message': "Invalid email or password"})
    return render(request, 'login.html')


def logout(request):
    if 'email' in request.session.keys():
        del request.session['email']
        return redirect('index')
    else:
        return redirect('index')


def vendorlogin1(request):
    if request.method == "POST":
        emaill = request.POST['email']
        passwordd = request.POST['password']
        try:
            data = VendorRegister.objects.get(email=emaill, password=passwordd)
            if data:
                request.session['vendoremail'] = data.email
                return redirect('index')
            else:
                return render(request, "vendorlogin.html", {'message': "Invalid email or password"})
        except:
            return render(request, "vendorlogin.html", {'message': "Invalid email or password"})
    return render(request, 'vendorlogin.html')


def vendorlogout(request):
    if 'vendoremail' in request.session.keys():
        del request.session['vendremail']
        return redirect('index')
    else:
        return redirect('index')


def about(request):
    if 'email' in request.session:
        # a=request.session['email']
        return render(request, 'aboutus.html')
    return render(request, 'aboutus.html')


def forget(request):
    if request.POST:
        useremail = request.POST['email']
        try:
            data = UserRegister.objects.get(email=useremail)
            if data:
                send_mail(
                    "Forgot Password",
                    "Dear " + str(data.name) +
                    "\n Your Password is :"+str(data.password),
                    "youremail",
                    [useremail],
                    fail_silently=False,
                )
                return render(request, 'forgetpass.html', {'message': 'Password  Sent To Your Email'})
            else:
                return render(request, 'forgetpass.html', {'message': 'Email Id Not Found'})
        except:
            return render(request, 'forgetpass.html', {'message': 'Email Id Not Found'})
    return render(request, 'forgetpass.html')


# productdata=Product.objects.get(id=request.session['productid'])
    # productdata.quantity=productdata.quantity-int(request.session['quantity'])

# def myorder(request):
#     if "email" in request.session:
#         a = request.session['email']
#         data1=UserRegister.objects.get(email=a)
#         data3=data1.name
#         data2=Product.objects.filter(name=data3)
#         data = Ordermodel.objects.filter(userName=data1.name)
#         return render(request, 'myorder.html', {'data':data ,'data2':data2,'a': a})

def myorder(request):
    if "email" in request.session:
        a = request.session['email']
        # b=Ordermodel.objects.get(id=request.GET['id'])
        prolist = []
        data = Ordermodel.objects.filter(userEmail=a)
        for i in data:
            pro = {}
            productdata = Product.objects.get(id=i.productid)
            pro['name'] = productdata.name
            pro['image'] = productdata.img
            pro['price'] = i.orderAmount
            pro['quantity'] = i.productqty
            pro['date'] = i.orderDate
            pro['transactionid'] = i.transactionId

            prolist.append(pro)
        return render(request, 'myorder.html', {'prolist': prolist, 'a': a})


def index(request):
    if 'email' in request.session:
        a = request.session['email']
        data = Category.objects.all()
        return render(request, 'base.html', {'data': data, 'a': a})
    elif 'vendoremail' in request.session:
        a = request.session['vendoremail']
        data = Category.objects.all()
        return render(request, 'base.html', {'data': data, 'a': a})
    else:
        data = Category.objects.all()
        return render(request, 'base.html', {'data': data})


def productall(request):
    if 'email' in request.session:
        a = request.session['email']
        data = Product.objects.all()
        return render(request, 'productall.html', {'data': data, 'a': a})
    elif 'vendoremail' in request.session:
        a = request.session['vendoremail']
        data = Product.objects.all()
        return render(request, 'productall.html', {'data': data, 'a': a})
    else:
        data = Product.objects.all()
        return render(request, 'productall.html', {'data': data})


def productcategorywise(request, id):
    if 'email' in request.session:
        a = request.session['email']
        data = Product.objects.filter(category=id)
        return render(request, 'productall.html', {'data': data, 'a': a})
    elif 'vendoremail' in request.session:
        a = request.session['vendoremail']
        data = Product.objects.filter(category=id)
        return render(request, 'productall.html', {'data': data, 'a': a})
    else:
        data = Product.objects.filter(category=id)
        return render(request, 'productall.html', {'data': data})


def singleproduct(request, id):
    if 'email' in request.session:
        a = request.session['email']
        data = Product.objects.get(pk=id)
        return render(request, 'singleproduct.html', {'data': data, 'a': a})
    elif 'vendoremail' in request.session:
        a = request.session['vendoremail']
        data = Product.objects.get(pk=id)
        return render(request, 'singleproduct.html', {'data': data, 'a': a})
    else:
        data = Product.objects.get(pk=id)
        return render(request, 'singleproduct.html', {'data': data})


def register(request):
    if request.method == "POST":
        namee = request.POST['name']
        emaill = request.POST['email']
        passwordd = request.POST['password']
        phonee = request.POST['phone']
        addresss = request.POST['address']
        data = UserRegister(name=namee, email=emaill,
                            password=passwordd, phone=phonee, address=addresss)
        a = UserRegister.objects.filter(email=emaill)
        if len(a) == 0:
            data.save()
            return redirect('login1')
        else:
            return render(request, 'register.html', {'message': "user alredy exist"})

    return render(request, 'register.html')


def vendorregister(request):
    if request.method == "POST":
        namee = request.POST['name']
        emaill = request.POST['email']
        passwordd = request.POST['password']
        phonee = request.POST['phone']
        addresss = request.POST['address']
        data = VendorRegister(name=namee, email=emaill,
                              password=passwordd, phone=phonee, address=addresss)
        a = VendorRegister.objects.filter(email=emaill)
        if len(a) == 0:
            data.save()
            return redirect('login2')
        else:
            return render(request, 'vendorregister.html', {'message': "user alredy exist"})

    return render(request, 'vendorregister.html')


def search(request):
    if 'email' in request.session:
        a = request.session['email']
        if request.method == "POST":
            namee = request.POST['q']
            posts = Product.objects.filter(name=namee)
            if posts:
                return render(request, 'search.html', {'posts': posts, 'namee': namee, "a": a})
            else:
                return redirect('productall')
        else:
            return render(request, 'base.html')
    else:
        if request.method == "POST":
            namee = request.POST['q']
            posts = Product.objects.filter(name=namee)
            return render(request, 'search.html', {'posts': posts, 'namee': namee})
        else:
            return render(request, 'base.html')


def searchview(request):
    word = request.GET.get('q')
    spl = word.split(" ")
    for i in spl:
        b = Product.objects.filter(Q(category__categoryname__icontains=i) | Q(
            name__icontains=i) | Q(price__icontains=i)).distinct()

    return render(request, 'productall.html', {'data': b, 'word': word})


def contact(request):
    if 'email' in request.session:
        a = request.session['email']
        data = UserRegister.objects.get(email=a)
        if request.method == "POST":
            contact_us = Contact()
            contact_us.name = request.POST['name']
            contact_us.email = request.POST['email']
            contact_us.phone = request.POST['phone']
            contact_us.text = request.POST['message']
            contact_us.save()
            return render(request, 'contactus.html', {'message': "Message sent", 'a': a})
        return render(request, 'contactus.html', {'data': data, 'a': a})
    elif 'vendoremail' in request.session:
        a = request.session['vendoremail']
        data = VendorRegister.objects.get(email=a)
        if request.method == "POST":
            contact_us = Contact()
            contact_us.name = request.POST['name']
            contact_us.email = request.POST['email']
            contact_us.phone = request.POST['phone']
            contact_us.text = request.POST['message']
            contact_us.save()
            return render(request, 'contactus.html', {'message': "Message sent", 'a': a})
        return render(request, 'contactus.html', {'data': data, 'a': a})
    else:
        if request.method == "POST":
            contact_us = Contact()
            contact_us.name = request.POST['name']
            contact_us.email = request.POST['email']
            contact_us.phone = request.POST['phone']
            contact_us.text = request.POST['message']
            contact_us.save()
            return render(request, 'contactus.html', {'message': "Message sent"})
        return render(request, 'contactus.html')


def changepass(request):
    if 'email' in request.session:
        a = request.session['email']
        user = UserRegister.objects.get(email=a)
        if request.method == "POST":
            old = request.POST['oldpass']
            new = request.POST['newpass']
            confirm = request.POST['confirmpass']
            if old == user.password:
                if new == confirm:
                    user.password = new
                    user.save()
                    return render(request, 'changepass.html', {'message': "Password Updated", 'a': a})
                else:
                    return render(request, 'changepass.html', {'message': "New Password not match", 'a': a})
            else:
                return render(request, 'changepass.html', {'message': "Old Password not match", 'a': a})

        return render(request, 'changepass.html', {'a': a})
    else:
        return redirect('login1')


def changeprofile(request):
    if 'email' in request.session:
        a = request.session['email']
        data = UserRegister.objects.get(email=a)

        if request.method == "POST":
            newname = request.POST.get('newname')
            newnumber = request.POST.get('newnumber')
            newaddress = request.POST.get('newaddress')
            if newname:
                data.name = newname
                data.save()
            if newnumber:
                data.phone = newnumber
                data.save()
            if newaddress:
                data.address = newaddress
                data.save()

            return render(request, 'changeprofile.html', {'message': "Change successfully", 'a': a})
        else:
            return render(request, 'changeprofile.html', {'a': a})
    else:
        return redirect('login1')


def buynow(request):
    if "email" in request.session:
        a = request.session['email']
        data = UserRegister.objects.get(email=a)
        if request.method == "POST":
            request.session['productid'] = request.POST['id']
            totalq = request.session['quantity'] = request.POST['qty']
            request.session['userid'] = data.pk
            request.session['username'] = data.name
            request.session['userEmail'] = data.email
            request.session['userContact'] = data.phone
            request.session['address'] = data.address
            b = Product.objects.get(id=request.POST['id'])
            request.session['orderAmount'] = b.price * int(totalq)
            request.session['paymentMethod'] = "Razorpay"
            request.session['transactionId'] = ""
            return redirect('razorpayview')
    else:
        return redirect('login1')


RAZOR_KEY_ID = ''
RAZOR_KEY_SECRET = ''
client = razorpay.Client(auth=(RAZOR_KEY_ID, RAZOR_KEY_SECRET))


def razorpayView(request):
    currency = 'INR'
    amount = int(request.session['orderAmount'])*100
    # Create a Razorpay Order
    razorpay_order = client.order.create(
        dict(amount=amount, currency=currency, payment_capture='0'))
    # order id of newly created order.
    razorpay_order_id = razorpay_order['id']
    callback_url = 'http://127.0.0.1:8000/paymenthandler/'
    # we need to pass these details to frontend.
    context = {}
    context['razorpay_order_id'] = razorpay_order_id
    context['razorpay_merchant_key'] = RAZOR_KEY_ID
    context['razorpay_amount'] = amount
    context['currency'] = currency
    context['callback_url'] = callback_url
    return render(request, 'razorpayDemo.html', context=context)


@csrf_exempt
def paymenthandler(request):
    # only accept POST request.
    if request.method == "POST":
        try:
            # get the required parameters from post request.
            payment_id = request.POST.get('razorpay_payment_id', '')
            razorpay_order_id = request.POST.get('razorpay_order_id', '')
            signature = request.POST.get('razorpay_signature', '')

            params_dict = {
                'razorpay_order_id': razorpay_order_id,
                'razorpay_payment_id': payment_id,
                'razorpay_signature': signature
            }

            # verify the payment signature.
            result = client.utility.verify_payment_signature(
                params_dict)

            amount = int(request.session['orderAmount'])*100  # Rs. 200
            # capture the payemt
            client.payment.capture(payment_id, amount)

            # Order Save Code
            orderModel = Ordermodel()
            orderModel.productid = request.session['productid']
            orderModel.productqty = request.session['quantity']
            orderModel.userId = request.session['userid']
            orderModel.userName = request.session['username']
            orderModel.userEmail = request.session['userEmail']
            orderModel.userContact = request.session['userContact']
            orderModel.address = request.session['address']
            orderModel.orderAmount = request.session['orderAmount']
            orderModel.paymentMethod = request.session['paymentMethod']
            orderModel.transactionId = payment_id
            productdata = Product.objects.get(id=request.session['productid'])
            productdata.quantity = productdata.quantity - \
                int(request.session['quantity'])
            productdata.save()
            orderModel.save()
            del request.session['productid']
            del request.session['quantity']
            del request.session['userid']
            del request.session['username']
            del request.session['userEmail']
            del request.session['userContact']
            del request.session['address']
            del request.session['orderAmount']
            del request.session['paymentMethod']
            # render success page on successful caputre of payment
            return redirect('orderSuccessView')
        except:
            print("Hello")
            # if we don't find the required parameters in POST data
            return HttpResponseBadRequest()
    else:
        print("Hello1")
       # if other than POST request is made.
        return HttpResponseBadRequest()


def successview(request):
    if 'email' in request.session:
        a = request.session['email']
        return render(request, 'order_sucess.html', {'a': a})
    else:
        return HttpResponseBadRequest()


def addproduct(request):
    if 'vendoremail' in request.session:
        vendor = VendorRegister.objects.get(
            email=request.session['vendoremail'])
        abc = Category.objects.all()
        if request.method == "POST" and request.FILES:
            vendorid = vendor.pk
            categoryid = Category.objects.get(id=int(request.POST['category']))
            productname = request.POST['productname']
            productprice = request.POST['price']
            image = request.FILES['image']
            quantity = request.POST['quantity']
            desc = request.POST['Description']
            # product=Product(vendorid=vendorid,categoryid=categoryid,productname=productname,productprice=productprice,image=image,quantity=quantity,description=desc)
            # product.save()
            Product.objects.create(vendorid=vendorid, category=categoryid, name=productname,
                                   img=image, price=productprice, description=desc, quantity=quantity)
        return render(request, 'addproduct.html', {'data': abc})
    else:
        return redirect('login2')
