from django.shortcuts import render,redirect,get_object_or_404
from.models import *
from jobseeker.models import Apply
from django.http import JsonResponse
def signup(request):
        if request.method=='POST':
           name=request.POST['name']
           dob=request.POST['dob']
           email=request.POST['email']
           mob=request.POST['mb']
           password=request.POST['password']
           companys=Companys(name=name,dob=dob,email=email,mob=mob,password=password)
           companys.save()
           return redirect('companys:payment')
        return render(request,'companys/signup.html')
def login(request):
    if request.method=='POST':
       email=request.POST['email']
       password=request.POST['password']

     #   if Companys.objects.filter(email=email,password=password).exists():
     #         return redirect('companys:hiring')
     #   else:
     #         error="invalid credentials"
     #         return render(request,'companys/login.html',{'msg':error})      

       try:
             comp=Companys.objects.get(email=email,password=password)
             request.session['company']=comp.id
             return redirect('companys:hiring')
       except Companys.DoesNotExist:
             return render(request,'companys/login.html',{'msg':'Invalid credential'})
    return render(request,'companys/login.html')

def forgot(request):
    return render(request,'companys/forgot.html')
def hiring(request):
    if 'company' in request.session:
     
        company_id=request.session.get('company')
        company_name=Companys.objects.get(id=company_id)
        if request.method=='POST':
          job=request.POST['job']
          quali=request.POST['quali']
          exp=request.POST['exp']
          places=request.POST['places']
          skills=request.POST['skills']
          company_name_=company_name
          hire=Hiring(job=job,quali=quali,exp=exp,places=places,skills=skills,company_name=company_name_)
          hire.save()
          # return JsonResponse({'message':'Successfully added'})
          return redirect('companys:cview')
        else:
          return render(request,'companys/hiring.html',{'company_name':company_name})
    else:
       
       return render(request,'jobseeker/home.html')  
def cview(request):
      if 'company' in request.session:
        company_id=request.session.get('company')
        company_name=Companys.objects.get(id=company_id)
        data=Hiring.objects.filter(company_name=company_name)
        return render(request,'companys/cview.html',{'hiring':data})
def update(request,hid):
      if 'company' in request.session:
          company_id=request.session.get('company')
          company_name=Companys.objects.get(id=company_id)
          hiringobj=Hiring.objects.get(id=hid)
          if request.method=='POST':
             job=request.POST['job']
             qualification=request.POST['quali']
             experience=request.POST['exp']
             places=request.POST['places']
             skills=request.POST['skills']
             hiringobj.job=job
             hiringobj.quali=qualification
             hiringobj.exp=experience
             hiringobj.places=places
             hiringobj.skills=skills
             hiringobj.company_name=company_name
             hiringobj.save()
             return redirect('companys:cview')
     
          return render(request,'companys/update.html',{'hire':hiringobj})
      else:
          return render(request,'jobseeker/home.html')
def deletecomp(request,hid):
    if 'company' in request.session:
       Hiring.objects.get(id=hid).delete()
       return redirect('companys:cview')
    else:
       return render(request,'jobseeker/home.html')

def applied(request):
     if 'company' in request.session:
         company_id=request.session.get('company')
         company_name=Companys.objects.get(id=company_id)
         
         seeker=Apply.objects.filter(company_name=company_name)
         return render(request,'companys/applied.html',{'application':seeker})
     else:
          return render(request,'jobseeker/home.html')


# def view_resume(request,rid):
#      resume=get_object_or_404(Apply,id=rid)
#      return render(request,'companys/view_resume.html',{'resume':resume})
def clogout(request):
     if 'company' in request.session:
          del request.session['company']
          return redirect('jobseeker:home')
def payment(request):
    if request.method=='POST':
     return redirect('companys:login')
    else:
      return render(request,'companys/payment.html')
