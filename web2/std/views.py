from django.shortcuts import render,HttpResponse
from std.models import Student 

# Create your views here.
def index(request):
    return render(request, 'index.html')

def doctor(request):
    record= Student.objects.filter(field='Medical')
    return render(request, 'doctor.html', {'record':record}) 

def engineer(request):
    record= Student.objects.filter(field='Engineer')
    return render(request, 'engineer.html', {'record':record})

def add(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        email=request.POST.get('email')
        field=request.POST.get('field')
        pan=request.POST.get('pan')
        
        new_record=Student(name=name, email=email, field=field, pan=pan)
        new_record.save()
        return HttpResponse("new record added successfully")
        
    return render(request, 'add.html')