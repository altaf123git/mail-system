from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required
from newapp.models import Vendor
from newapp.models import Contact
from django.core.mail import send_mail
from application import settings

# Create your views here.
def home(request):
    return render(request,'home.html')

def userlogin(request):
    if request.method=='POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        user=authenticate(username=user, password=password)
        if user is not None:
            login(request, user)
            return redirect('/show')
        else:
            return redirect("/userlogin")
    return render(request,'login.html')

#@login_required(login_url='/userlogin')
# def data(request):
#     return render(request,'data.html')

def add(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        pan=request.POST.get('pan')
        
        new_vendor=Vendor(name=name, email=email, mobile=mobile, pan=pan)
        new_vendor.save()
    return render(request,'add.html')

def update(request,id):
    record=Vendor.objects.get(id=id)
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        pan=request.POST.get('pan')
        updated=Vendor(id=id, name=name, email=email, mobile=mobile, pan=pan)
        updated.save()
    return render(request,'update.html',{"record":record})

def delete(request,id):
    del_id=Vendor.objects.get(id=id)
    del_id.delete()
    return HttpResponse("deleted successfully")

@login_required(login_url='/userlogin')
def show(request):
    record=Vendor.objects.all()
    return render(request,'data.html', {"record":record})

def newuser(request):
    if request.method=='POST':
        user=request.POST.get('user')
        email=request.POST.get('email')
        password1=request.POST.get('password1')
        password2=request.POST.get('password2')
        if (password1==password2):
            # new=User(username=user, password=password1)
            new=User.objects.create_user(user,email,password1)
            new.save()
        else:
            return HttpResponse("password not match")
    return render(request,'newuser.html')

def contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        desc=request.POST.get('desc')
        contact=Contact(name=name, email=email, mobile=mobile, desc=desc)
        contact.save()
        
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')

def service(request):
    return render(request,'service.html')

def userlogout(request):
    logout(request)
    return redirect('/userlogin')

def mail(request, id):
    record= Vendor.objects.get(id=id)
    if request.method=='POST':
        subject=request.POST.get('subject')
        message=request.POST.get('message')
        to= record.email
        res     = send_mail(subject, message, settings.EMAIL_HOST_USER, [to])  
        if(res == 1):  
            msg = "Mail Sent Successfuly"  
        else:  
            msg = "Mail could not sent"  
        return HttpResponse(msg)
        
    return render(request, 'mail.html', {"record":record})