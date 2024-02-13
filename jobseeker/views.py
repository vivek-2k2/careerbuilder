from django.shortcuts import render,redirect
from.models import *
from companys.models import *
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
        #  if Jobseeker.objects.filter(email=email,password=password).exists():
        #      return redirect('jobseeker:dashboard')
        #  else:
        #      error="invalid credentials"
        #      return render(request,'jobseeker/login.html',{'msg':error})  
     
         try:
              job=Jobseeker.objects.get(email=email,password=password)
              request.session['jobsee']=job.id
              return redirect('jobseeker:profile')
         except Jobseeker.DoesNotExist:
             return render(request,'jobseeker/login.html',{'msg':'Invalid credential'})      
    return render(request,'jobseeker/login.html')
def home(request):
    return render(request,'jobseeker/home.html')
def dashboard(request):
    
    data=Hiring.objects.all()
    return render(request,'jobseeker/dashboard.html',{'hiring':data})
def forgot(request):
    return render(request,'jobseeker/forgot.html')
def about(request):
    return render(request,'jobseeker/about.html')
def apply(request,hid):
   if 'jobsee' in request.session:
     hiringobj=Hiring.objects.get(id=hid)
     return render(request,'jobseeker/apply.html',{'hire':hiringobj})
   else:
        return render(request,'jobseeker/login.html')
def form(request):
    if 'jobsee' in request.session:
      if request.method=='POST':
        name=request.POST['name']
        dob=request.POST['dob']
        email=request.POST['email']
        mob=request.POST['mob']
        quali=request.POST['quali']
        cv=request.FILES['cv']
        apply=Apply(name=name,dob=dob,email=email,mob=mob,quali=quali,cv=cv)
        apply.save()
        return redirect('jobseeker:dashboard')  
      return render(request,'jobseeker/form.html')
    else:
     return render(request,'jobseeker/home.html')

def profile(request):
  if 'jobsee' in request.session:
    return render(request,'jobseeker/profile.html')
  else:
    return render(request,'jobseeker/login.html')
def jlogout(request):
     if 'jobsee' in request.session:
          del request.session['jobsee']
          return redirect('jobseeker:home')
     else:
         return render(request,'jobseeker/home.html')
def status(request):
        job=Apply.objects.all()
   

        return render(request,'jobseeker/status.html')
