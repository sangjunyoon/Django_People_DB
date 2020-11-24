from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.template import loader
from django.urls import reverse
from django.views import generic
from django.utils import timezone

from .models import Employee
from .models import User

# Create your views here.

def home(request):
    return render(request, 'people/home.html', {}) 

def database(request):
    return render(request, 'people/database.html', {})

def employee(request):
    employee_list = Employee.objects.all
    return render(request, 'people/employee.html', {'Employee_List': employee_list})

def user(request):
    user_info = User.objects.all
    return render(request, 'people/user.html', {"User_Info": user_info})