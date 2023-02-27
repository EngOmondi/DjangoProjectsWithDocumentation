Create an Online Job Portal Project in Python Django
In this job portal project, the applicants requiring a job can connect to the companies. It is a great platform for both the applicants and also for all the companies.

About the Job Portal System:
In this job portal, the applicants and companies can register themselves. Both are provided with different roles. The applicant can see a list of jobs available and can apply to any that matches his/her skill set. Similarly, the companies can add new jobs and select the applicants who have applied for that job by seeing their resume.

Django Job Portal System:
The main purpose of this project is to create job opportunities for the applicants. It will be a great opportunity for the applicants to get a chance at various companies. This portal can also create more employment which is very much needed.

Project Prerequisites
You must be well versed with the following topics that are:

1.Python

2.Html, CSS

3.Bootstrap

Download Job Portal Python Django Project

Please download the source code of python django job portal: Online Job Portal Python Code

Project File Structure
First, let’s check the steps to build the Job Portal System in Python Django Framework:

1. Firstly, use the django-admin startproject command to create a project.
2. Then, use the django-admin start-app command to create an app inside the project.
3. Keep all the html templates in one folder.
4. Run the python manage.py migrate command to apply all the Django built in migrations.
5. Create a superuser with an username, email and password.
6. Lastly, start making the urls for the project.

Urls.py

from django.urls import path
from . import views
 
urlpatterns = [
    path("", views.index, name="index"),
    # for users or applicants
    path("user_login/", views.user_login, name="user_login"),
    path("signup/", views.signup, name="signup"),
    path("user_homepage/", views.user_homepage, name="user_homepage"),
    path("logout/", views.Logout, name="logout"),
    path("all_jobs/", views.all_jobs, name="all_jobs"),
    path("job_detail/<int:myid>/", views.job_detail, name="job_detail"),
    path("job_apply/<int:myid>/", views.job_apply, name="job_apply"),
    # for Company
    path("company_signup/", views.company_signup, name="company_signup"),
    path("company_login/", views.company_login, name="company_login"),
    path("company_homepage/", views.company_homepage, name="company_homepage"),
    path("add_job/", views.add_job, name="add_job"),
    path("job_list/", views.job_list, name="job_list"),
    path("edit_job/<int:myid>/", views.edit_job, name="edit_job"),
    path("company_logo/<int:myid>/", views.company_logo, name="company_logo"),
    path("all_applicants/", views.all_applicants, name="all_applicants"),
    # for admin
    path("admin_login/", views.admin_login, name="admin_login"),
    path("view_applicants/", views.view_applicants, name="view_applicants"),
    path("delete_applicant/<int:myid>/", views.delete_applicant, name="delete_applicant"),
    path("pending_companies/", views.pending_companies, name="pending_companies"),
    path("accepted_companies/", views.accepted_companies, name="accepted_companies"),
    path("rejected_companies/", views.rejected_companies, name="rejected_companies"),
    path("all_companies/", views.all_companies, name="all_companies"),
    path("change_status/<int:myid>/", views.change_status, name="change_status"),
    path("delete_company/<int:myid>/", views.delete_company, name="delete_company"),
]
Code Explanation:
The above code consists of the urls of the whole project. These paths are separated for the users that are the applicants, for the admin and for the companies.

Advertisement

Models.py :

from django.db import models
from django.contrib.auth.models import User
 
class Applicant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
 
    def __str__(self):
        return self.user.first_name
 
class Company(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    gender = models.CharField(max_length=10)
    type = models.CharField(max_length=15)
    status = models.CharField(max_length=20)
    company_name = models.CharField(max_length=100)
 
    def __str__ (self):
        return self.user.username
 
class Job(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    title = models.CharField(max_length=200)
    salary = models.FloatField()
    image = models.ImageField(upload_to="")
    description = models.TextField(max_length=400)
    experience = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    skills = models.CharField(max_length=200)
    creation_date = models.DateField()
 
    def __str__ (self):
        return self.title
 
class Application(models.Model):
    company = models.CharField(max_length=200, default="")
    job = models.ForeignKey(Job, on_delete=models.CASCADE)
    applicant = models.ForeignKey(Applicant, on_delete=models.CASCADE)
    resume = models.ImageField(upload_to="")
    apply_date = models.DateField()
 
    def __str__ (self):
        return str(self.applicant)
Code Explanation:
Total four models have been created for the project. Applicants model is used to store all basic details of the applicants. Company model is used to store the details of the various companies registering to the portal. Job model stores the data about the job that a company can add for the applicants to apply. Applicants applying for the job in any company are saved in the Application model.

Advertisement

1. Home page navigation bar (basic.html):
<nav class="navbar navbar-expand-lg sticky-top navbar-dark">
      <div class="container-fluid w-50">
        <a class="navbar-brand" href="#">Job Portal</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarSupportedContent">
          <ul class="navbar-nav me-auto mb-2 mb-lg-0">
            {% if not request.user.is_authenticated %}
            <li class="nav-item">
              <a class="nav-link {% block home %} {% endblock %}" aria-current="page" href="/">Home</a>
            </li>
            <li class="nav-item">
              <a class="nav-link {% block user_login %} {% endblock %}" href="/user_login/">User Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link {% block admin_login %} {% endblock %}" href="/admin_login/">Admin Login</a>
            </li>
            <li class="nav-item">
              <a class="nav-link {% block company_login %} {% endblock %}" href="/company_login/">Company Login</a>
            </li>
            {% else %}
            <li class="nav-item">
              <a class="nav-link active" href="/logout/">Logout</a>
            </li>
          </ul>
          {% endif %}
        </div>
      </div>
    </nav>
Code Explanation:
In total there are 4 navigation bars for the home page, signup and login pages, for users, for companies and lastly for the admin. The above code is for the projects home page, signup and login pages. As soon as the project is opened there would be 3 options available that are user login, admin login and the company login.

Advertisement

Users can login or signup through user login option and similarly, the admin and the companies. If the users are already authenticated then rather than the login options, a logout option is shown.

2. Home page (index.html):
<div class="container-fluid mt-2">
    <img src="{% static 'industries-recruitment.png' %}" alt="" width="100%" height="450px">
</div>
    <div class="container-fluid mt-2" style="background-color: #4f868c; width: 100%;">
        <div class="row">
            <div class="col-md-4">
                <h3 style="color: aliceblue;">Contact Us</h3>
                <p style="color: aliceblue">Email:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;jobportal@gmail.com</p>
                <p style="color: aliceblue">Mobile No.:&nbsp;&nbsp;9745632121</p>
            </div>
        </div>
    </div>
Views.py :

def index(request):
    return render(request, "index.html")
Code Explanation:
The navigation bar (basic.html) is extended on the home page. An image with a contact us container is also shown. The email id and mobile number is provided in the contact us section as the contacting details.

Advertisement

3. User Signup and login page (user_login.html) and (signup.html):
User Login:

<form method="POST"> {% csrf_token %}
    <div class="container mt-5">
        <h6>Haven't register yet, then click here        <a href="/signup/" type="submit" class="btn" style="background-color: #4f868c; color: white;">Signup</a>
        </h6>
        <div class="mb-3">
            <label for="username" class="form-label"><i style="font-weight: bold;">Username</i></label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label"><i style="font-weight: bold;">Password</i></label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter Password">
        </div>
        <br>
        <input type="submit" value="Submit" class="btn" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
 
    </div>
</form>
Views.py :

def user_login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
 
            if user is not None:
                user1 = Applicant.objects.get(user=user)
                if user1.type == "applicant":
                    login(request, user)
                    return redirect("/user_homepage")
            else:
                thank = True
                return render(request, "user_login.html", {"thank":thank})
    return render(request, "user_login.html")
User Signup:

Advertisement

<form class="container mt-4" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
 
    <div class="row">
        <div class="form-group col-md-6">
            <label>First Name</label>
            <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Enter First Name">
        </div>
        <div class="form-group col-md-6">
            <label>Last Name</label>
            <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Enter Last Name">
        </div>
    </div>
    
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Password</label>
            <input type="password" class="form-control" name="password1" id="password1" placeholder="Enter Password">
        </div>
        <div class="form-group col-md-6">
            <label>Confirm Password</label>
            <input type="password" class="form-control" name="password2" id="password2" placeholder="Confirm Password">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Email Id</label>
            <input type="email" class="form-control" name="email" id="email" placeholder="Enter Email Id">
        </div>
        <div class="form-group col-md-6">
            <label>Contact Number</label>
            <input type="tel" class="form-control" name="phone" id="phone" placeholder="Enter Contact Number">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Gender</label>
            <div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
            <div class="form-check form-check-inline">
                <input type="radio" class="custom-control-input" name="gender" id="male" value="Male">
                <label for="male" class="custom-control-label">Male</label>
            </div>
            <div class="form-check form-check-inline">
                <input type="radio" class="custom-control-input" name="gender" id="female" value="Female">
                <label for="female" class="custom-control-label">Female</label>
            </div>
        </div>
        </div>
        <div class="form-group col-md-6">
            <label>Profile Picture</label>
            <input type="file" class="form-control" name="image" id="image" placeholder="Enter Last Name">
        </div>
    </div>
    <br>
<input type="submit" value="Submit" class="btn" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
</form>
Views.py :

Advertisement

def signup(request):
    if request.method=="POST":   
        username = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']
 
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, username=username, password=password1)
        applicants = Applicant.objects.create(user=user, phone=phone, gender=gender, image=image, type="applicant")
        user.save()
        applicants.save()
        return render(request, "user_login.html")
    return render(request, "signup.html")
Code Explanation:
All the applicants can click on user login and if they haven’t signed up yet then they can click on signup. There they can fill the required details and register them as an applicant in the portal. After successful signup the user will be known as an applicant and can now login with the username and password.

4. User profile page (user_homepage.html):
<div class="container">
    <div class="row">
        <div class="col-sm-6">
 
            <form class="container mt-4" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
 
                <div class="row">
                    <div class="form-group col-md-6">
                        <label>First Name</label>
                        <input type="text" class="form-control mt-2" name="first_name" id="first_name"
                            value="{{applicant.user.first_name}}" required>
                    </div>
                    <div class="form-group col-md-6">
                        <label>Last Name</label>
                        <input type="text" class="form-control mt-2" name="last_name" id="last_name"
                        value="{{applicant.user.last_name}}" required>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-12">
                        <label>Username</label>
                        <input type="text" class="form-control mt-2" name="username" id="username"
                            value="{{applicant.user.username}}" readonly>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-6">
                        <label>Email Id</label>
                        <input type="email" class="form-control mt-2" name="email" id="email" value="{{applicant.user.email}}" required>
                    </div>
                    <div class="form-group col-md-6">
                        <label>Contact Number</label>
                        <input type="tel" class="form-control mt-2" name="phone" id="phone" value="{{applicant.phone}}" required>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-6">
                        <label>Gender</label>
                        {% if applicant.gender == "Male" %}
                        <div class="mt-2" style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender" value="Male" checked>
                                <label for="male" class="custom-control-label">Male</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender"
                                    value="Female">
                                <label for="female" class="custom-control-label">Female</label>
                            </div>
                        </div>
                        {% else %}
                        <div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender" value="Male">
                                <label for="male" class="custom-control-label">Male</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender"
                                    value="Female" checked>
                                <label for="female" class="custom-control-label">Female</label>
                            </div>
                        </div>
                        {% endif %}
                    </div>
                    <div class="form-group col-md-6">
                        <label>Profile Photo</label>
                        <input type="file" class="form-control mt-2" name="image" id="image">
                    </div>
                </div>
 
                <input type="submit" value="Submit" class="btn mt-4" accept="image/*" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
            </form>
 
        </div>
        <div class="col-sm-4 mt-5 text-center">
            <img src="{{applicant.image.url}}" alt="" width="200px" height="200px">
        </div>
    </div>
</div>
Views.py :

def user_homepage(request):
    if not request.user.is_authenticated:
        return redirect('/user_login/')
    applicant = Applicant.objects.get(user=request.user)
    if request.method=="POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']
 
        applicant.user.email = email
        applicant.user.first_name = first_name
        applicant.user.last_name = last_name
        applicant.phone = phone
        applicant.gender = gender
        applicant.save()
        applicant.user.save()
 
        try:
            image = request.FILES['image']
            applicant.image = image
            applicant.save()
        except:
            pass
        alert = True
        return render(request, "user_homepage.html", {'alert':alert})
    return render(request, "user_homepage.html", {'applicant':applicant})
Code Explanation:
As soon as the applicant logs in, the applicant is redirected to the profile page. On the profile page, all the details about the applicant are displayed which the applicant has given during the time of signup. The applicant is also able to edit some of the information after login.

Advertisement

5. Job List Page (all_jobs.html):

<div class="container mt-4">
<table class="table table-hover" id="example">
    <thead>
        <tr>
            <th>Sr.No</th>
            <th>Company Name</th>
            <th>Job Title</th>
            <th>Salary</th>
            <th>Location</th>
            <th>Created On</th>
            <th>Apply</th>
        </tr>
    </thead>
    <tbody>
        {% for job in jobs %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{job.company.company_name}}</td>
            <td>{{job.title}}</td>
            <td>{{job.salary}}</td>
            <td>{{job.location}}</td>
            <td>{{job.creation_date}}</td>
 
            {% if job.id in data %}
            <td><a class="btn btn-success">Applied</a></td>
            {% else %}
            <td><a href="/job_detail/{{job.id}}/" class="btn btn-success">Apply</a></td>
            {% endif %}
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>
Views.py :

Advertisement

def all_jobs(request):
    jobs = Job.objects.all().order_by('-start_date')
    applicant = Applicant.objects.get(user=request.user)
    apply = Application.objects.filter(applicant=applicant)
    data = []
    for i in apply:
        data.append(i.job.id)
    return render(request, "all_jobs.html", {'jobs':jobs, 'data':data})
Code Explanation:
Then there is an option of job lists in the navigation bar for all the applicants who are logged in to their accounts. On clicking on the job list option, the applicant is able to view all the available jobs. There is an apply button created for each job. If the title of the job matches the applicant’s skills or interests then the applicant can click on the apply button to view the job in detail.

6. Job Detail Page (job_detail.html):
<div class="container mt-4 shadow-lg py-3 mb-4">
<div class="row">
    <div class="col-md-4">
        <img src="{{job.image.url}}" alt="" width="350px" height="250px">
    </div>
    <div class="col-md-6">
        <h2>{{job.title}}</h2>
        <p>{{job.company.company_name}}<i><a href=""> (View All Jobs)</a></i></p>
        <i class="fa fa-map-marker">{{job.location}}</i>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
        <i class="fa fa-calendar">{{job.creation_date}}</i>
        <br>
        <strong>Salary: <i class="fa fa-inr mr-2"></i>₹ {{job.salary}}/month</strong>
        <div class="mt-3">
            <a href="/job_apply/{{job.id}}/" class="btn btn-danger">Apply For The Job</a>
        </div>
    </div>
</div>
<div class="mt-4">
    <h3>Overview</h3>
    <p>{{job.description}}</p>
 
    <h4>Required Experience</h4>
    <p>{{job.experience}} years</p>
 
    <h4>Skills Required</h4>
    <p>{{job.skills}}</p>
 
    <h4>Start Date</h4>
    <p>{{job.start_date}}</p>
</div>
</div>
Views.py :

Advertisement

def job_detail(request, myid):
    job = Job.objects.get(id=myid)
    return render(request, "job_detail.html", {'job':job})
Code Explanation:
When the applicant clicks on the apply button, then the applicant can view all the details of that job. After viewing all the details about the job, the applicant can click on the apply for job button if the applicant wants to apply for it.

7. Uploading the resume for the job (job_apply.html):
<div class="container mt-4 shadow-lg py-3 mb-4">
<form method="POST" enctype="multipart/form-data"> {% csrf_token %}
    <div class="form-row">
        <label>Upload Resume</label>
        <input type="file" class="form-control mt-3" name="resume" id="resume">
    </div>
    <input type="submit" value="Submit" class="btn btn-danger mt-3">
</form>
</div>
Views.py :

def job_apply(request, myid):
    if not request.user.is_authenticated:
        return redirect("/user_login")
    applicant = Applicant.objects.get(user=request.user)
    job = Job.objects.get(id=myid)
    date1 = date.today()
    if job.end_date < date1:
        closed=True
        return render(request, "job_apply.html", {'closed':closed})
    elif job.start_date > date1:
        notopen=True
        return render(request, "job_apply.html", {'notopen':notopen})
    else:
        if request.method == "POST":
            resume = request.FILES['resume']
            Application.objects.create(job=job, company=job.company, applicant=applicant, resume=resume, apply_date=date.today())
            alert=True
            return render(request, "job_apply.html", {'alert':alert})
    return render(request, "job_apply.html", {'job':job})
Code Explanation:
The applicant can finally send the resume to the company that he/she wished to apply for. The company can check the resume and contact the applicant if the company wants.

Advertisement

8. Company Login and Signup (company_login.html) and (company_signup.html):
Company Login:

<form method="POST"> 
    {% csrf_token %}
    <div class="container mt-5">
        <h6>Haven't register yet, then click here        <a href="/company_signup/" type="submit" class="btn" style="background-color: #4f868c; color: white;">Signup</a>
 
        <div class="mb-3">
            <label for="username" class="form-label"><i style="font-weight: bold;">Username</i></label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label"><i style="font-weight: bold;">Password</i></label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter Password">
        </div>
        <br>
        <input type="submit" value="Submit" class="btn" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
 
    </div>
</form>
Views.py :

Advertisement

def company_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
 
        if user is not None:
            user1 = Company.objects.get(user=user)
            if user1.type == "company" and user1.status != "pending":
                login(request, user)
                return redirect("/company_homepage")
        else:
            alert = True
            return render(request, "company_login.html", {"alert":alert})
    return render(request, "company_login.html")
Company Signup:

<form class="container mt-4" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
 
    <div class="row">
        <div class="form-group col-md-6">
            <label>First Name</label>
            <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Enter First Name">
        </div>
        <div class="form-group col-md-6">
            <label>Last Name</label>
            <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Enter Last Name">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-12">
            <label>Username</label>
            <input type="text" class="form-control" name="username" id="username" placeholder="Enter Username">
        </div>
    </div>
    
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Password</label>
            <input type="password" class="form-control" name="password1" id="password1" placeholder="Enter Password">
        </div>
        <div class="form-group col-md-6">
            <label>Confirm Password</label>
            <input type="password" class="form-control" name="password2" id="password2" placeholder="Confirm Password">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Email Id</label>
            <input type="email" class="form-control" name="email" id="email" placeholder="Enter Email Id">
        </div>
        <div class="form-group col-md-6">
            <label>Contact Number</label>
            <input type="tel" class="form-control" name="phone" id="phone" placeholder="Enter Contact Number">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-6">
            <label>Gender</label>
            <div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
            <div class="form-check form-check-inline">
                <input type="radio" class="custom-control-input" name="gender" id="male" value="Male">
                <label for="male" class="custom-control-label">Male</label>
            </div>
            <div class="form-check form-check-inline">
                <input type="radio" class="custom-control-input" name="gender" id="female" value="Female">
                <label for="female" class="custom-control-label">Female</label>
            </div>
        </div>
        </div>
        <div class="form-group col-md-6">
            <label>Logo of the Company</label>
            <input type="file" class="form-control" name="image" id="image" placeholder="Enter Last Name">
        </div>
    </div>
 
    <div class="row mt-4">
        <div class="form-group col-md-12">
            <label>Company Name</label>
            <input type="text" class="form-control" name="company_name" id="company_name" placeholder="Enter Name of the Company">
        </div>
    </div>
    <br>
<input type="submit" value="Submit" class="btn" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
</form>
Views.py :

def company_signup(request):
    if request.method=="POST":   
        username = request.POST['username']
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        phone = request.POST['phone']
        gender = request.POST['gender']
        image = request.FILES['image']
        company_name = request.POST['company_name']
 
        if password1 != password2:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')
        
        user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
        company = Company.objects.create(user=user, phone=phone, gender=gender, image=image, company_name=company_name, type="company", status="pending")
        user.save()
        company.save()
        return render(request, "company_login.html")
    return render(request, "company_signup.html")
Code Explanation:
Similar to the applicants, all the companies first have to register their company to the portal. All the basic details of the Company will be taken during the registration process. After successful registration the company can login through the username and password.

Advertisement
9. Company Profile Page (company_homepage.html):
<div class="container">
    <div class="row">
        <div class="col-sm-6">
 
            <form class="container mt-4" method="POST" enctype="multipart/form-data">
                {% csrf_token %}
 
                <div class="row">
                    <div class="form-group col-md-6">
                        <label>First Name</label>
                        <input type="text" class="form-control" name="first_name" id="first_name"
                            value="{{company.user.first_name}}" required>
                    </div>
                    <div class="form-group col-md-6">
                        <label>Last Name</label>
                        <input type="text" class="form-control" name="last_name" id="last_name"
                        value="{{company.user.last_name}}" required>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-12">
                        <label>Username</label>
                        <input type="text" class="form-control" name="username" id="username"
                            value="{{company.user.username}}" readonly>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-12">
                        <label>Company Name</label>
                        <input type="text" class="form-control" name="company_name" id="company_name"
                            value="{{company.company_name}}" readonly>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-6">
                        <label>Email Id</label>
                        <input type="email" class="form-control" name="email" id="email" value="{{company.user.email}}" required>
                    </div>
                    <div class="form-group col-md-6">
                        <label>Contact Number</label>
                        <input type="tel" class="form-control" name="phone" id="phone" value="{{company.phone}}" required>
                    </div>
                </div>
 
                <div class="row mt-4">
                    <div class="form-group col-md-6">
                        <label>Gender</label>
                        {% if company.gender == "Male" %}
                        <div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender" value="Male" checked>
                                <label for="male" class="custom-control-label">Male</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender"
                                    value="Female">
                                <label for="female" class="custom-control-label">Female</label>
                            </div>
                        </div>
                        {% else %}
                        <div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender" value="Male">
                                <label for="male" class="custom-control-label">Male</label>
                            </div>
                            <div class="form-check form-check-inline">
                                <input type="radio" class="custom-control-input" name="gender"
                                    value="Female" checked>
                                <label for="female" class="custom-control-label">Female</label>
                            </div>
                        </div>
                        {% endif %}
                    </div>
                    <div class="form-group col-md-6">
                        <label>Logo of the Company</label>
                        <input type="file" class="form-control" name="image" id="image">
                    </div>
                </div>
 
                <input type="submit" value="Submit" class="btn mt-4" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
            </form>
 
        </div>
        <div class="col-sm-4 mt-5 text-center">
            <img src="{{company.image.url}}" alt="" width="200px" height="200px">
        </div>
    </div>
</div>
Views.py :

def company_homepage(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    company = Company.objects.get(user=request.user)
    if request.method=="POST":   
        email = request.POST['email']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        phone = request.POST['phone']
        gender = request.POST['gender']
 
        company.user.email = email
        company.user.first_name = first_name
        company.user.last_name = last_name
        company.phone = phone
        company.gender = gender
        company.save()
        company.user.save()
 
        try:
            image = request.FILES['image']
            company.image = image
            company.save()
        except:
            pass
        alert = True
        return render(request, "company_homepage.html", {'alert':alert})
    return render(request, "company_homepage.html", {'company':company})
Code Explanation:
After login the company profile page is shown where the company can edit some of the details.

Advertisement

10. Add Jobs by the Company (add_job.html)
<form class="container mt-3" method="POST" enctype="multipart/form-data">
    {% csrf_token %}
 
    <div class="row">
        <div class="form-group col-md-12">
            <label>Job Title</label>
            <input type="text" class="form-control" name="job_title" id="job_title" placeholder="Job Title" required>
        </div>
    </div>
    
    <div class="row mt-3">
        <div class="form-group col-md-6">
            <label>Start Date</label>
            <input type="date" class="form-control" name="start_date" id="start_date" placeholder="Start Date" required>
        </div>
        <div class="form-group col-md-6">
            <label>End Date</label>
            <input type="date" class="form-control" name="end_date" id="end_date" placeholder="End Date" required>
        </div>
    </div>
 
    <div class="row mt-3">
        <div class="form-group col-md-6">
            <label>Company Logo</label>
            <input type="file" class="form-control" name="logo" id="logo" placeholder="Enter Company Logo" required>
        </div>
        <div class="form-group col-md-6">
            <label>Salary (per month)</label>
            <input type="tel" class="form-control" name="salary" id="salary" placeholder="Enter Salary (per month)" required>
        </div>
    </div>
 
    <div class="row mt-3">
        <div class="form-group col-md-12">
            <label>Skills Required</label>
            <input type="text" class="form-control" name="skills" id="skills" placeholder="Enter the required skills for the job" required>
        </div>
        </div>
    
    <div class="row mt-3">
        <div class="form-group col-md-6">
            <label>Experience (in years)</label>
            <input type="text" class="form-control" name="experience" id="experience" placeholder="Experience required (in years)" required>
        </div>
        <div class="form-group col-md-6">
            <label>Company Location</label>
            <input type="text" class="form-control" name="location" id="location" placeholder="Enter exact location of the Company" required>
        </div>
    </div>
 
    <div class="row mt-3">
        <div class="form-group col-md-12">
            <label>Job Description</label>
           <textarea name="description" id="description" class="form-control" cols="30" rows="4" placeholder="Description of the exact job" required></textarea>
        </div>
    </div>
<input type="submit" value="Submit" class="btn mt-3" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
</form>
Views.py :

def add_job(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    if request.method == "POST":
        title = request.POST['job_title']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']
        salary = request.POST['salary']
        image = request.FILES['logo']
        experience = request.POST['experience']
        location = request.POST['location']
        skills = request.POST['skills']
        description = request.POST['description']
        user = request.user
        company = Company.objects.get(user=user)
        job = Job.objects.create(company=company, title=title,start_date=start_date, end_date=end_date, salary=salary, image=image, experience=experience, location=location, skills=skills, description=description, creation_date=date.today())
        job.save()
        alert = True
        return render(request, "add_job.html", {'alert':alert})
    return render(request, "add_job.html")
Code Explanation:
The Companies then can add new jobs which will be viewed by the applicants. If the applicants are interested in the job, then they can send the resume and apply for that job. While adding the jobs the companies need to provide the details about it.

11. Entire list of jobs added by the company (job_list.html):
<div class="container mt-4">
<table class="table table-hover" id="example">
    <thead>
        <tr>
            <th>Sr.No</th>
            <th>Job Title</th>
            <th>Created On</th>
            <th>Action</th>
            <th>Delete</th>
        </tr>
    </thead>
    <tbody>
        {% for job in jobs %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{job.title}}</td>
            <td>{{job.creation_date}}</td>
            <td><a href="/edit_job/{{job.id}}/" class="btn"><i class="fa fa-edit"></i></a></td>
            <td><a href="#" class="btn"><i class="fa fa-trash"></i></a></td>
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>
Views.py :

def job_list(request):
    if not request.user.is_authenticated:
        return redirect("/company_login")
    companies = Company.objects.get(user=request.user)
    jobs = Job.objects.filter(company=companies)
    return render(request, "job_list.html", {'jobs':jobs})
Code Explanation:
After adding the jobs, the companies can view all the jobs added by them. They can delete the job if required or else can edit the job details.

12. All applicants applied for the job (all_applicants.html):
<div class="container mt-4">
    <table class="table table-hover" id="example">
        <thead>
            <tr>
                <th>Sr.No</th>
                <th>Job Title</th>
                <th>Applicant</th>
                <th>Applied On</th>
                <th>Resume</th>
                <th>Delete</th>
            </tr>
        </thead>
        <tbody>
            {% for i in application %}
            <tr>
                <td>{{forloop.counter}}</td>
                <td>{{i.job}}</td>
                <td>{{i.applicant}}</td>
                <td>{{i.apply_date}}</td>
                <td><a href="{{i.resume.url}}" class="btn"><i class="fa fa-file"></i></a></td>
                <td><a href="#" class="btn"><i class="fa fa-trash"></i></a></td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
    </div>
Views.py :

def all_applicants(request):
    company = Company.objects.get(user=request.user)
    application = Application.objects.filter(company=company)
    return render(request, "all_applicants.html", {'application':application})
Code Explanation:
The company can view all the applicants that have applied for a job to that company. The company can see all the applicants’ resumes and then select the applicants who fulfill the requirements of the company.

13. Admin Login Page (admin_login.html):
<form method="POST"> 
    {% csrf_token %}
    <div class="container mt-5">
        <div class="mb-3">
            <label for="username" class="form-label"><i style="font-weight: bold;">Username</i></label>
            <input type="text" class="form-control" id="username" name="username" placeholder="Enter Username">
        </div>
        <div class="mb-3">
            <label for="password" class="form-label"><i style="font-weight: bold;">Password</i></label>
            <input type="password" class="form-control" id="password" name="password" placeholder="Enter Password">
        </div>
        <br>
        <input type="submit" value="Submit" class="btn" style="background-color: #4f868c; color: white; font-size: larger; width: 8rem;">
    </div>
</form>
Views.py :

def admin_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
 
        if user.is_superuser:
            login(request, user)
            return redirect("/all_companies")
        else:
            alert = True
            return render(request, "admin_login.html", {"alert":alert})
    return render(request, "admin_login.html")
Code Explanation:
Admin can login by giving the username and password. No signup option is given for the admin as the admin is a super user and can make the changes or manage the entire portal.

14. All Companies (all_companies.html):
<div class="container mt-4">
<table class="table table-hover" id="example">
    <thead>
        <tr>
            <th>Sr.No</th>
            <th>Full Name</th>
            <th>Email Id</th>
            <th>Contact</th>
            <th>Gender</th>
            <th>Company Name</th>
            <th>Image</th>
            <th>Status</th>
            <th>Change Status</th>
            <th>Delete</th>
        </tr>
    </thead>
    <tbody>
        {% for company in companies %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{company.user.get_full_name}}</td>
            <td>{{company.user.email}}</td>
            <td>{{company.phone}}</td>
            <td>{{company.gender}}</td>
            <td>{{company.company_name}}</td>
            <td><img src="{{company.image.url}}" class="rounded-circle" width="90px" height="70px"></td>
            <td>{{company.status}}</td>
            <td><a href="/change_status/{{company.id}}/" class="btn btn-secondary">Change Status</a></td>
            <td><a href="/delete_company/{{company.user.id}}/" class="btn btn-danger" onclick="return confirm('Are you sure you want to delete this company?')">Delete</a></td>
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>
Views.py :

def all_companies(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    companies = Company.objects.all()
    return render(request, "all_companies.html", {'companies':companies})
Code Explanation:
After the admin logs in, the admin can see all the list of companies that are registered to the portal. The admin can check all the details of the company and then can accept or reject that company on the given details by that company. The admin can also delete a company.

15. All Applicants (view_applicants.html):
<div class="container mt-4">
<table class="table table-hover" id="example">
    <thead>
        <tr>
            <th>Sr.No</th>
            <th>Full Name</th>
            <th>Email Id</th>
            <th>Contact</th>
            <th>Gender</th>
            <th>Image</th>
            <th>Action</th>
        </tr>
    </thead>
    <tbody>
        {% for applicant in applicants %}
        <tr>
            <td>{{forloop.counter}}</td>
            <td>{{applicant.user.get_full_name}}</td>
            <td>{{applicant.user.email}}</td>
            <td>{{applicant.phone}}</td>
            <td>{{applicant.gender}}</td>
            <td><img src="{{applicant.image.url}}" class="rounded-circle" width="90px" height="70px"></td>
            <td><a href="/delete_user/{{applicant.user.id}}/" class="btn btn-danger" onclick="return confirm('Are you sure you want to delete this applicant?')">Delete</a></td>
        </tr>
        {% endfor %}
    </tbody>
</table>
</div>
Views.py :

def view_applicants(request):
    if not request.user.is_authenticated:
        return redirect("/admin_login")
    applicants = Applicant.objects.all()
    return render(request, "view_applicants.html", {'applicants':applicants})
Code Explanation:

The admin is also able to see the list of all applicants that are registered to the portal. The admin can delete any applicant he/ she wants.

Django Job Portal Output:
Applicant Login:

job portal login

Admin Login:

admin login

List of Jobs for applicants to apply:

list of jobs for applicants

Job Details on Django Job Portal:

job details

All Companies where admin can accept or reject a company:

all companies

Companies can add jobs after login:

add jobs on django job portal