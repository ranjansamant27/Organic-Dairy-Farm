from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .models import Products,Cart,Checkout,Payment
from django.http import HttpResponse
from django.db.models import Q
# import razorpay


# Create your views here.

def index(request):
    context  = {}
    products=Products.objects.filter(is_active=True)
    product_name = request.GET.get('product_name')
    if product_name !='' and product_name is not None:
        products = Products.objects.filter(name__icontains=product_name)
    context={
        'product': products
    }
    
    return render(request,'index.html',context)
    
    
def signup_view(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        confirmpassword=request.POST['confirmpassword']
        
        
            
        
        if password != confirmpassword:
            messages.warning(request,'Passwords didnt match')            
            return redirect('/signup')
        
            
        try: 
            if User.objects.get(username=username):
                messages.warning(request,'username already taken')
                return redirect('/signup')
        except Exception as identifier:
            pass
        user_obj= User.objects.create_user(username=username,password=password)
        # user_obj.set_password(password)
        user_obj.save()
        messages.success(request,'user created')
        return redirect('/')

        
    
    
    
    return render(request,'signup.html')



def login_view(request):
    
    if request.method == 'POST':
        username=request.POST['username']
        password = request.POST['password']
        myuser= authenticate(username=username,password=password)
        if myuser is not None:
            login(request,myuser)
            HttpResponse(request,f'welcome {username} you\'ve been logged in')
            return redirect('/')
        else:
            messages.warning(request,f'couldn\'t login')
            return redirect('/login')
    return render(request,'login.html')
        


            

def logout_view(request):
    
    logout(request)
    
    return redirect('/')



def productdetails(request,item_id):
    
    product=Products.objects.get(id=item_id)
    context={
        'product':product
    }
    return render(request,'productdetails.html',context)



def addtocart(request,pid):
    if request.user.is_authenticated:
        uid=request.user.id
        
        u=User.objects.get(id=uid)
        
        p=Products.objects.get(id=pid)
        obj= Cart.objects.filter(uid=u,pid=p)
        if obj:
            obj[0].quantity+=1
            obj[0].save()
        else:
            
            c=Cart.objects.create(uid=u,pid=p)
            
                      
        
        
        return redirect('/viewcart')

    else:
        return redirect('/login')
    
    
    
def viewcart(request):
    user=request.user.id
    c=Cart.objects.filter(uid=user)
    
    
    sum=0
    
    context={}
    
    for item in c:
        
        sum = sum+ (item.pid.price)* (item.quantity)
        
    context = { 'total':sum , 'products': c }
    
    
    return render(request,'cart.html',context)
    
    
    

def catfilter(request,cid):
    
    q1=Q(is_active=True)
    q2=Q(category=cid)
    products=Products.objects.filter(is_active=True,category=cid)
    context={
        'product':products
    }
    return render(request,'index.html',context)

def removefromcart(request,id):
    if request.user.is_authenticated:
        
        # Cart.objects.filter(id=cid).delete()
        cartobj= Cart.objects.filter(id=id)
        

        
        cartobj.delete()
        return redirect('/viewcart')
    else: 
        return redirect('/login')
        
def updateqty(request,id,qv):
    if request.user.is_authenticated:
        
        c=Cart.objects.filter(id=id)
        # print(c[0].pid.name)
        if qv=='1':
            t=c[0].quantity+1
            c.update(quantity=t)
        elif qv=="0":
            if c[0].quantity>1:
                t=c[0].quantity-1
                c.update(quantity=t)
    return redirect('/viewcart')
    
    
def clearcart(request):
    if request.user.is_authenticated:
        user_id = request.user.id        
        cart_items=Cart.objects.filter(uid=user_id)
        cart_items.delete()
        
        return redirect('/viewcart')
    else:return redirect('/login')
    
    
def checkout(request):
    myuser=request.user
 
    c=Cart.objects.filter(uid=myuser.id)
    sum=0
    for item in c:
        sum+=int(item.pid.price)*item.quantity
    
    if request.method== 'POST':
        
        
        name=request.POST['name']
        address= request.POST['address']
        pincode= request.POST['pincode']
        phonenumber= request.POST['phonenumber']
        obj = Checkout(user=myuser,name=name,address=address,phonenumber=phonenumber,pincode=pincode)

        obj.save()
        return redirect('/')
    context = {
        'total':sum
    }
    return render(request,'checkout.html',context)


def makepayment(request):
    # o=Checkout.objects.filter(uid=request.user.id)
    # sum=0
    # np=len(o)
    # context={}
    # for i in o:
    #     sum+=i.pid.price*i.quantity
    #     oid=i.order_id
    # sum=sum*100
    myuser=request.user
    c=Cart.objects.filter(uid=myuser.id)
    
    sum=0
    for item in c:
        sum+=int(item.pid.price)*item.quantity
    pay = Payment.objects.create(user=myuser,amount=sum*100)
    pay.save()
    print('sum',sum)
    client = razorpay.Client(auth=("rzp_test_BpQQcNXA6SMKyo","ArRAuCHky47XG3asUfG3uFzf"))
    data = { "amount": sum, "currency": "INR", "receipt": id}
    # payment = client.order.create(data=data)
    
    # print(payment)
    # context['payment']=payment
    context= { 'payment':pay }
    print(pay.amount)
    print(type(pay))
    return render(request,"payment.html",context)