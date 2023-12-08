from django.shortcuts import render,redirect
from.models import *
from django.http import JsonResponse

def signup(request):
    if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']
        password=request.POST['password']
        jobseeker=Jobseeker(name=name,dob=dob,email=email,mob=mob,password=password)
        jobseeker.save()
        return redirect('jobseeker:login')
    return render(request,'jobseeker/signup.html')
def login(request):
    if request.method=='POST':
         email=request.POST['email']
         password=request.POST['password']
         if Jobseeker.objects.filter(email=email,password=password).exists():
             return redirect('jobseeker:home')
         else:
             error="invalid credentials"
             return render(request,'jobseeker/login.html',{'msg':error})        
    return render(request,'jobseeker/login.html')
def home(request):
    return render(request,'jobseeker/home.html')
def dashboard(request):
    return render(request,'jobseeker/dashboard.html')
def forgot(request):
    return render(request,'jobseeker/forgot.html')
# Create your views here.