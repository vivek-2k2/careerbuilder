from django.db import models
class Companys(models.Model):
    name=models.TextField(db_column='name',null=True)
    dob=models.TextField(db_column='dob',null=True)
    email=models.TextField(db_column='email',null=True)
    mob=models.TextField(db_column='mob',null=True)
    password=models.TextField(db_column='password',null=True)
    def __str__(self):
        return self.name
    class Meta:
        db_table='companys_signup'
class Hiring(models.Model):
     company_name=models.ForeignKey(Companys,db_column='name',on_delete=models.CASCADE,null=True)
     job=models.TextField(db_column='job',null=True)
     quali=models.TextField(db_column='quali',null=True)
     exp=models.TextField(db_column='exp',null=True)
     places=models.TextField(db_column="places",null=True)
     skills=models.TextField(db_column='skills',null=True)
     def __str__(self):
        return self.job



            
# Create your models here.
