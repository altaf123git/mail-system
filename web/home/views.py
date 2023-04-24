from django.shortcuts import render, redirect, HttpResponse
from home.models import Employee
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/login')
def index(request):
    record= Employee.objects.all()
    return render(request, 'index.html', {'record':record}) 

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        mobile=request.POST.get('mobile')
        city=request.POST.get('city')
        
        new=Employee(name=name, email=email, mobile=mobile, city=city)
        new.save()
        messages.success(request, 'Your profile was updated.')
        
    return render(request,'add.html')

def userlogin(request):
    if request.method=='POST':
        user=request.POST.get('user')
        password=request.POST.get('password')
        user=authenticate(username=user, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/login')
        
    return render(request,'login.html')

def userlogout(request):
    logout(request)
    return redirect('/login')

def update(request, id):
    record=Employee.objects.get(id=id)
    
    if (request.method == 'POST'):
        name=request.POST['name']
        email=request.POST['email']
        mobile=request.POST['mobile']
        city=request.POST['city']
        
        new_record = Employee(id=id, name=name, email=email, mobile=mobile, city=city )
        
        new_record.save()
        return HttpResponse("updated successfully")
    return render(request, "update.html", {"record":record} )

def delete(request, id):
    del_id=Employee.objects.get(id=id)
    del_id.delete()
    return HttpResponse("deleted")
