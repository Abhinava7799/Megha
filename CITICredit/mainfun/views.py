from django.shortcuts import render

from .models import Bankcarddetails, Customer, Department, Employee

# Create your views here.


def home(request):
    return render(request, 'home.html')


def creditcarddetails(request):
    creditdetails = Bankcarddetails.objects.all()
    context = {
        'creditdetails': creditdetails
    }
    return render(request, 'creditcarddetails.html', context)


def empdetails(request):
    employeedes = Employee.objects.all()
    context = {
        'employeedes': employeedes
    }
    return render(request, 'empdetails.html', context)


def departments(request):
    departdetails = Department.objects.all()
    context = {
        'departdetails': departdetails
    }
    return render(request, 'departments.html', context)


def custdetails(request):
    customerdetails = Customer.objects.all()
    context = {
        'customerdetails': customerdetails
    }
    return render(request, 'custdetails.html', context)


