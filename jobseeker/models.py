from django.db import models
from companys.models import *
class Jobseeker(models.Model):
    name=models.TextField(db_column='name',null=True)
    dob=models.TextField(db_column='dob',null=True)
    email=models.TextField(db_column='email',null=True)
    mob=models.TextField(db_column='mob',null=True)
    password=models.TextField(db_column='password',null=True)
    def __str__(self):
        return self.email
    class Meta:
        db_table='jobseeker_signup'
class Apply(models.Model):
     company_name=models.ForeignKey(Companys,on_delete=models.CASCADE,null=True)
     applicant=models.ForeignKey(Jobseeker,on_delete=models.CASCADE,null=True)
     job=models.TextField(max_length=100,null=True)
     name=models.TextField(max_length=100,db_column='name',null=True)
     dob=models.TextField(max_length=100,db_column='dob',null=True)
     email=models.TextField(max_length=100,db_column='email',null=True)
     mob=models.TextField(max_length=100,db_column="mob",null=True)
     quali=models.TextField(max_length=100,db_column='quali',null=True)
     cv=models.FileField(upload_to='resumes/',db_column='cv',null=True)

        

