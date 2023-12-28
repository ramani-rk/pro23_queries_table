from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
def dept(request):
    QLTO=Dept.objects.all()
    
    d={'Dept':QLTO}
    return render(request,'dept.html',d)


def emp(request):
    QLTO=Emp.objects.all()
    QLTO=Emp.objects.all().order_by('ename')
    QLTO=Emp.objects.all().order_by('-ename')
    QLTO=Emp.objects.all().order_by(Length('ename'))
    QLTO=Emp.objects.all().order_by(Length('ename').desc())
    QLTO=Emp.objects.all().order_by('empno')[::]
    QLTO=Emp.objects.exclude(ename='Rk')
    QLTO=Emp.objects.filter(Hiredate__month=5)
    QLTO=Emp.objects.filter(Hiredate__year=2023)
    QLTO=Emp.objects.filter(Hiredate__day=10)
    QLTO=Emp.objects.filter(salary__lt=50000)
    QLTO=Emp.objects.filter(salary__lte=50000)
    QLTO=Emp.objects.filter(salary__gt=50000)
    QLTO=Emp.objects.filter(salary__gte=50000)
    QLTO=Emp.objects.filter(deptno__in=('2','3'))
    QLTO=Emp.objects.filter(pk__in=(11,))
    QLTO=Emp.objects.filter(pk__in=(11,20))
    QLTO=Emp.objects.filter(pk__in=('11','20'))
    QLTO=Emp.objects.filter(ename__in=('Rk',))
    QLTO=Emp.objects.filter(ename__in=('Rk','Ek'))
    QLTO=Emp.objects.filter(ename__in=['Ek'])
    QLTO=Emp.objects.filter(ename__in=['Ek','Rk'])
    QLTO=Emp.objects.filter(ename__contains='R',salary__gt=50000)
    QLTO=Emp.objects.filter(Q(ename__startswith='E') & Q(salary__lt=50000))
    QLTO=Emp.objects.filter(Q(ename__contains='k') & Q(salary__lt=23000))
    #QLTO=Emp.objects.all()
    
    

    d={'Emp':QLTO}
    return render(request,'emp.html',d)

def insert_dept(request):
    dno=input('Enter deptno')
    dna=input('Enter dname')
    l=input('Enter loc')

    NDO=Dept.objects.get_or_create(deptno=dno,dname=dna,loc=l)[0]
    NDO.save()

    QLTO=Dept.objects.all()
    d={'Dept':QLTO}
    return render(request,'dept.html',d)

def insert_emp(request):
    dno=input('Enter deptno : ')
    eno=input('Enter empno : ')
    ena=input('Enter empna : ')
    j=input('Enter job : ')
    MGR=input('Enter MGR_id : ')
    em=input('Enter email : ')
    hd=input('Enter hiredate : ')
    s=input('Enter salary : ')
    c=input('Enter comm : ')

    NDO=Dept.objects.get(deptno=dno)
    NEO=Emp.objects.get_or_create(deptno=NDO,empno=eno,ename=ena,job=j,MGR_id=MGR,email=em,Hiredate=hd,salary=s,comm=c)[0]
    NEO.save()

    QLTO=Emp.objects.all()
    d={'Emp':QLTO}
    return render(request,'emp.html',d)