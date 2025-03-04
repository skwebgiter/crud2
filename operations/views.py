from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

# Create your views here.
def emp_list(request):
    list = Employee.objects.all
    return render(request,'list.html',{'data':list})

def create(request):
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list')
        errmsg = "create a valid response"
        return redirect('create',)
    else:
        form = EmployeeForm
    return render(request,'create.html',{'form':form})

def update(request, id):
    # obj = Employee.objects.all()
    emp_id = Employee.objects.get(id=id)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=emp_id)
        if form.is_valid():
            form.save()
            return redirect('list')
        return redirect('update')
    else:
        form = EmployeeForm(instance=emp_id)
    return render(request,'update.html',{'form':form,'emp_id':emp_id})

def delete(request, id):
    emp_id = Employee.objects.get(id=id)
    if request.method == 'POST':
        emp_id.delete()
        return redirect('list')
    return render(request,'delete.html',{'emp_id':emp_id})
