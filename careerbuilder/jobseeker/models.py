from django.db import models
class Jobseeker(models.Model):
    name=models.TextField(db_column='name',null=True)
    dob=models.TextField(db_column='dob',null=True)
    email=models.TextField(db_column='email',null=True)
    mob=models.TextField(db_column='mob',null=True)
    password=models.TextField(db_column='password',null=True)
    class Meta:
        db_table='jobseeker_signup'
        
# Create your models here.
