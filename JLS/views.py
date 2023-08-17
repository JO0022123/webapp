from django.shortcuts import render,redirect
from . models import*
from .form import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import  JsonResponse
from email import message
import json
# Create your views here.
def home(request):
    context={}
    catagory=Catagory.objects.filter(status=0)
    return render(request,'index.html',{"catagory":catagory})
def je(request):
    context={}
    products=Product.objects.filter(trending=1)
    return render(request,'je.html',{"products":products})
def ring(request):
    Product2=Catagory.objects.filter(status=0)
    
    return render(request,'cat/ring.html',{"Product":Product2})
def chain(request):
    context={}
    return render(request,'cat/chain.html',context)
def bracelet(request):
    context={}
    return render(request,'cat/bracelet.html',context)
def necklace(request):
    context={}
    return render(request,'cat/necklace.html',context)
def bangle(request):
    context={}
    return render(request,'cat/bangle.html',context)
def earring(request):
    context={}
    return render(request,'cat/earring.html',context)
def about(request):
    context={}
    return render(request,'layout/about.html',context)
def contact(request):
    context={}
    return render(request,'layout/contact.html',context)
def login_page(request):
    context={}
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method=='POST':
            name=request.POST.get('username')
            pwd=request.POST.get('password')
            user=authenticate(request,username=name,password=pwd)
            if user is not None:
                login(request,user)
                messages.success(request,"Logged in Successfully")
                return redirect("/")
            else:
                messages.error(request,"Invalid User Name or Password")
                return redirect("/login")
    '''
    if request.method == 'POST':
        if Member.objects.filter(email=request.POST['email'], password=request.POST['password']).exists():
            member = Member.objects.get(email=request.POST['email'], password=request.POST['password'])
            messages.success(request,"Logged in Successfully")
            return render(request, 'layout/login.html', {'member': member})
        else:
            messages.error(request,"Invalid User Name or Password")
            return redirect("/login")'''
    return render(request,'layout/login.html',context)
def signup(request):
    context={}
    form=CustomUserForm()
    if request.method=='POST':
        form=CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Registration Success You can Login Now..!")
            return redirect('/login')
    '''
    if request.method == 'POST':
        username= request.POST['username']
        email = request.POST['email']
        password = request.POST.get('password')
        post=Member()
        post.username= username
        post.email= email
        post.password= password
        member=Member(username=post.username,email=post.email,password=post.password)
        member.save()
        messages.success(request,"Registration Success You can login Now..!")
        return redirect('login')'''
    return render(request,'layout/signup.html',{'form':form})
def collectionsview(request,name):
  if(Catagory.objects.filter(name=name,status=0)):
      products=Product.objects.filter(category__name=name)
      return render(request,"products/index1.html",{"products":products,"category_name":name})
  else:
    messages.warning(request,"No Such Catagory Found")
    return redirect('category')
def product_details(request,cname,pname):
    if(Catagory.objects.filter(name=cname,status=0)):
        if(Product.objects.filter(name=pname,status=0)):
            products=Product.objects.filter(name=pname,status=0).first()
            return render(request,"products/product_details.html",{"products":products})
        else:
            messages.error(request,"No Such Produtct Found")
            return redirect('category')
def logout_page(request):
  if request.user.is_authenticated:
    logout(request)
    messages.success(request,"Logged out Successfully")
  return redirect("/")
def cart_page(request):
  if request.user.is_authenticated:
    cart=Cart.objects.filter(user=request.user)
    return render(request,"products/card.html",{"cart":cart})
  else:
    return redirect("/")
 
def remove_cart(request,cid):
  cartitem=Cart.objects.get(id=cid)
  cartitem.delete()
  return redirect("/cart")
def add_to_cart(request):
   if request.headers.get('x-requested-with')=='XMLHttpRequest':
    if request.user.is_authenticated:
      data=json.load(request)
      product_qty=data['product_qty']
      product_id=data['pid']
      #print(request.user.id)
      product_status=Product.objects.get(id=product_id)
      if product_status:
        if Cart.objects.filter(user=request.user.id,product_id=product_id):
          return JsonResponse({'status':'Product Already in Cart'}, status=200)
        else:
          if product_status.quantity>=product_qty:
            Cart.objects.create(user=request.user,product_id=product_id,product_qty=product_qty)
            return JsonResponse({'status':'Product Added to Cart'}, status=200)
          else:
            return JsonResponse({'status':'Product Stock Not Available'}, status=200)
    else:
      return JsonResponse({'status':'Login to Add Cart'}, status=200)
   else:
    return JsonResponse({'status':'Invalid Access'}, status=200)