from django.db import models

# Create your models here.

class Dept(models.Model):
    deptno=models.IntegerField(primary_key=True)
    deptname=models.CharField(max_length=100,unique=True)
    loc=models.CharField(max_length=100)


    def __str__ (self):
        return str(self.deptno)



class Emp(models.Model):
    deptno=models.ForeignKey(Dept,on_delete=models.CASCADE)
    empno=models.IntegerField(primary_key=True)
    ename=models.CharField(max_length=100)
    job=models.CharField(max_length=100)
    MGR_id=models.CharField(max_length=100)
    email=models.CharField(max_length=100,default='@gmail.com')
    Hiredate=models.DateField(max_length=100)
    salary=models.IntegerField(default=50000)
    comm=models.IntegerField(default=0)

    def __str__ (self):
        return self.ename