from django.db import models
class Jobseeker(models.Model):
    name=models.TextField(db_column='name',null=True)
    dob=models.TextField(db_column='dob',null=True)
    email=models.TextField(db_column='email',null=True)
    mob=models.TextField(db_column='mob',null=True)
    password=models.TextField(db_column='password',null=True)
    class Meta:
        db_table='jobseeker_signup'
class Apply(models.Model):
     name=models.TextField(max_length=100,db_column='name',null=True)
     dob=models.TextField(max_length=100,db_column='dob',null=True)
     email=models.TextField(max_length=100,db_column='email',null=True)
     mob=models.TextField(max_length=100,db_column="mob",null=True)
     quali=models.TextField(max_length=100,db_column='quali',null=True)
     cv=models.FileField(upload_to='resumes/',db_column='cv',null=True)

        
# Create your models here.
