Online School Management System Python Django Project
Online school management system is an advanced level python project. We will be using Django (python open-source framework) and Sqlite3 database to implement the same

Project Functionalities:
Add attendance
Add marks
Add notice
Check attendance
Check notice
Check marks
School Management System Project Prerequisites
To install the required libraries, please use pip installer from the terminal:

pip install Django
Download School Management System Source Code
Steps to Create School Management Project in Python Django
1. Start Project
Django itself creates a project and an app with all the necessary files if we run the following commands

django-admin startproject OnlineSchoolMgmt
cd OnlineSchoolMgmt
django-admin startapp app
2. Writing Models
Code:

from django.db import models
from django.contrib.auth.models import User
 
# Create your models here.
 
class Attendance(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    LecturesAttended = models.IntegerField(null=True)
    TotalLectures  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Marks(models.Model):
    StudentName = models.CharField(max_length=200,null=True)
    StudentId  = models.CharField(max_length=50,null=True)
    PhysicsMarks = models.IntegerField(null=True)
    ChemistryMarks  = models.IntegerField(null=True)
    MathsMarks  = models.IntegerField(null=True)
    EnglishMarks  = models.IntegerField(null=True)
    ComputerMarks  = models.IntegerField(null=True)
 
    def __str__(self):
        return self.StudentName
 
class Notice(models.Model):
    Message = models.CharField(max_length=200,null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.Message
In this school management system project, we have created 3 models. In other words, we have created 3 tables to store the details of student’s attendance, marks, and the notice (if any) drafted by the school authorities.

Advertisement

Now, to actually create the tables, we have to execute the following two commands:

Py manage.py makemigrations
Py manage.py migrate
3. forms.py
Django does not create this file, so we have to create this new file in the app folder and then you can type the following code in forms.py.

Forms.py is required to implement CRUD functionality i.e. for creating, retrieving, updating and deleting objects from the database. So we have created a form for each model we have defined.

Code:

from django.forms import ModelForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class createuserform(UserCreationForm):
    class Meta:
        model=User
        fields=['username','password'] 
 
class addAttendanceform(ModelForm):
    class Meta:
        model=Attendance
        fields="__all__"
 
class addMarksform(ModelForm):
    class Meta:
        model=Marks
        fields="__all__"
 
class addNoticeform(ModelForm):
    class Meta:
        model=Notice
        fields="__all__"
4. admin.py
Advertisement

Code:

from django.contrib import admin
from .models import *
 
# Register your models here.
admin.site.register(Atttendance)
admin.site.register(Notice)
admin.site.register(Marks)
Django provides an inbuilt admin panel for online school management project (for every project). We have to register the models we have created on admin panel so that we can access the data from admin panel also. But for that we require a staff user, to create a superuser (admin) run the following commands:

py manage.py createsuperuser
It will ask following details: username, email, and password.

5. urls.py
Code:

"""OnlineSchoolMgmt URL Configuration
 
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import*
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home ,name='home'),
   
    path('addAttendance/', addAttendance,name='addAttendance'),
   
    path('addMarks/', addMarks,name='addMarks'),
 
    path('addNotice/', addNotice,name='addNotice'),
 
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),
]
We have defined the url patterns in this file.

Advertisement
6. views.py:
Code:

from django.shortcuts import redirect,render
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
from .forms import *
 
def home(request):
    notice = Notice.objects.all()
    attendance = Attendance.objects.all()
    marks = Marks.objects.all()
 
    context = {
        'notice':notice,
        'marks':marks,
        'attendance':attendance,
    }
    return render(request,'app/home.html',context)
 
def addAttendance(request):    
    if request.user.is_authenticated:
        form=addAttendanceform()
        if(request.method=='POST'):
            form=addAttendanceform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addAttendance.html',context)
    else: 
        return redirect('home')
 
def addMarks(request): 
    if request.user.is_authenticated:
        form=addMarksform()
        if(request.method=='POST'):
            form=addMarksform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addMarks.html',context)
    else: 
        return redirect('home')  
 
def addNotice(request):    
    if request.user.is_authenticated:
        form=addNoticeform()
        if(request.method=='POST'):
            form=addNoticeform(request.POST)
            if(form.is_valid()):
                form.save()
                return redirect('/')
        context={'form':form}
        return render(request,'app/addNotice.html',context)
    else: 
        return redirect('home') 
 
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home') 
    else: 
        form=createuserform()
        if request.method=='POST':
            form=createuserform(request.POST)
            if form.is_valid() :
                user=form.save()
                return redirect('login')
        context={
            'form':form,
        }
        return render(request,'app/register.html',context)
 
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
       if request.method=="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/')
       context={}
       return render(request,'app/login.html',context)
 
def logoutPage(request):
    logout(request)
    return redirect('/')
The very first function is home which renders all the entries from Attendance, Marks, and Notice table and pass them to home.html. Home.html (which is the home page of school management project) displays all the information in tabular form.

Home.html
{% extends 'app/Links.html' %}
 
{% block content %}
 
<div class="container ">
 
    <br><br>
<div class="row">
    <div class="col-md-9">
        <h5>Notice:</h5>
        
        <div class="card card-body">
            <table class="table table-sm">
                <tr>
                    <th>Notice</th>
                    <th>Date</th>
                </tr>
                {% for n in notice %}
                <tr>
                    <td>{{n.Message}} </td>
                    <td>{{n.date_created}} </td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</div>
 
<br><br>
 
<div class="row">
    <div class="col-md-9">
        <h5>Attendance:</h5>
        
        <div class="card card-body">
            <table class="table table-sm">
                <tr>
                    <th>Student Id</th>
                    <th>Student Name</th>
                    <th>Attended Lectures</th>                    
                    <th>Total Lectures</th>
                </tr>
                {% for a in attendance %}
                <tr>
                    <td>{{a.StudentId}} </td>
                    <td>{{a.StudentName}} </td>
                    <td>{{a.LecturesAttended}} </td>
                    <td> {{a.TotalLectures}} </td>
                </tr>
                {% endfor %}
            </table>
        </div>
    </div>
</div>
 
<br><br>
 
<div class="row">
    <div class="col-md-9">
        <h5>Marks:</h5>
        
        <div class="card card-body">
            
            <table class="table table-sm">
                <tr>
                    <th>Student Id</th>
                    <th>Student Name</th>
                    <th>Physics Marks</th>      
                    <th>Chemistry Marks</th>      
                    <th>Maths Marks</th>      
                    <th>English Marks</th>      
                    <th>Computer Marks</th>  
                </tr>
                {% for m in marks %}
                <tr>
                    <td>{{m.StudentId}} </td>
                    <td>{{m.StudentName}} </td>
                    <td>{{m.PhysicsMarks}} </td>
                    <td>{{m.ChemistryMarks}} </td>
                    <td>{{m.MathsMarks}} </td>
                    <td>{{m.EnglishMarks}} </td>
                    <td>{{m.ComputerMarks}} </td>
                </tr>
                {% endfor %}
            </table>
            <p> <b>Note:</b> Marks are out of 100</p>
        </div>
    </div>
</div>



{% endblock %}
Admin Home Page:
admin home page

school admin home 2

Advertisement

Student Home Page:
school student home

We can see the navigation bar for both the users are different.

Advertisement
The next function in this file is addAttendance which uses addAttendanceform to create a new record in attendance table. This function is only for admin of school management project. If any other user attempts to access this, the user will get redirected to respective home page.

AddAttendance.html
{% extends 'app/Links.html' %}
{% block content %}
 
<div class="jumbotron container row">
    <div class="col-md-6">
        
    <h1>Add Attendance</h1>
        <div class="card card-body">
           <form action="" method="POST">
              {% csrf_token %}
                {{form.as_p}}
                <br>
             <input type="submit" name="Submit">
             </form>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}
Add Attendance Page:
add attendance admin

Add Marks and Add Notice functions are very similar to this function

AddNotice.html
{% extends 'app/Links.html' %}
{% block content %}
 
<div class="jumbotron container row">
    <div class="col-md-6">
        <h1>Add Notice</h1>
        <div class="card card-body">
           <form action="" method="POST">
              {% csrf_token %}
                {{form.as_p}}
                <br>
             <input type="submit" name="Submit">
             </form>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}
Add Notice Page:
add notice admin

Advertisement
AddMarks.html
{% extends 'app/Links.html' %}
{% block content %}
 
<div class="jumbotron container row">
    <div class="col-md-6">
        
    <h1>Add Marks</h1>
        <div class="card card-body">
           <form action="" method="POST">
              {% csrf_token %}
                {{form.as_p}}
                <br>
             <input type="submit" name="Submit">
             </form>
            </div>
        </div>
    </div>
 
</div>
{% endblock %}
Add Marks Page:
Advertisement
add marks admin

7. Templates:
Login.html
{% extends 'app/Links.html' %}
{% load static%}
{% block content %}
<div class="container jumbotron">
    <form method="POST" action="">
        {% csrf_token %}
        <p><input type="text" name="username" placeholder="Username..."></p>
        <p><input type="password" name="password" placeholder="Password..." ></p>
        <input class="btn btn-success" type="submit" value="Login">
        <p>Do not have an account<a href='{% url 'register' %}'>Register</a></p>
    </form>
</div>
{% endblock %}
Register.html
Advertisement

{% extends 'app/Links.html' %}
{% load static%}
{% block content %}
<div class="container jumbotron">
    <form method="POST" action="" >
        {% csrf_token %}
        {{form.as_p}}
       
        <input class="btn btn-success" type="submit" value="Register Account">
    </form>
</div>
{% endblock %}
Links.html
{% load static %}
<html>
    <head>
        <title>
            TechVidvan Online School Management Project
        </title>
        <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/css/bootstrap.min.css" integrity="sha384-9aIt2nRpC12Uk9gS9baDl411NQApFmC26EwAOH8WgZl5MYYxFfc+NcPb1dKGj7Sk" crossorigin="anonymous">
    </head>
    <body>        
        {% include 'app/navbar.html' %}
        {% block content %}   
        {% endblock %}
        <br>
       
        <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.0/dist/umd/popper.min.js" integrity="sha384-Q6E9RHvbIyZFJoft+2mJbHaEWldlvI9IOYy5n3zV9zzTtmI3UksdQRVvoxMfooAo" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.0/js/bootstrap.min.js" integrity="sha384-OgVRvuATP1z7JjHLkuOU7Xw704+h835Lr+6QL9UvYjZE3Ipu6Tp75j7Bh/kR0JKI" crossorigin="anonymous"></script>
    </body>
</html>
navbar.html
Advertisement

{% load static %}
 
<style>
  .greet{
    font-size: 18px;
    color: #fff;
    margin-right: 20px;
  }
</style>
 
<nav class="navbar navbar-expand-lg navbar-dark bg-dark">
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarNav" aria-controls="navbarNav" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>
  <div class="collapse navbar-collapse" id="navbarNav">
 
    <ul class="navbar-nav">
      
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'home' %}">Home</a>
      </li>
      {% if request.user.is_staff %}
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'addAttendance' %}">Add Attendance</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'addNotice' %}">Add Notice</a>
      </li>
      <li class="nav-item active">
        <a class="nav-link" href="{% url 'addMarks' %}">Add Marks</a>
      </li>
      {% endif %}
      <li class="nav-item">
        <a class="nav-link" href="{% url 'login' %}">Login</a>
      </li>
    </ul>
  </div>
  {% if request.user.is_staff %}
  <span class="greet">Hello, {{request.user}}</span>
  <span ><a  class="greet" href="{% url 'logout' %}">Logout</a></span>
  {% endif %}
 
</nav>