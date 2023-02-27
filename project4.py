Online Blood Donation System Project in Python Django
Blood Donation is important for people in urgent need of it which can save millions of patients. Hence blood donation management system is very much important. Here we will develop Blood Donation system using Python in easy steps.

About the Blood Donation Management System:
The patients in need of the blood are able to request for the blood. Users can register themselves to become a donor. All users are also able to see all the donors list according to different blood groups as well as the list of all the requested blood by different users or patients. The patients in need of the blood can contact the available donors of the same blood group and city. This will help a lot of people who are in need of blood.

Django Blood Donation Management System
The main objective of this project is to create a platform where the people or patients in need of the blood can easily find a donor of the same blood group. This connects the donors and the recipients.

Project Prerequisites:
You must know the following languages required for this project:

1. HTML

2. CSS

3. Bootstrap

4. Python Django Framework

Download Python Blood Donation System Project
Models.py :
from django.db import models
from django.contrib.auth.models import User
 
class BloodGroup(models.Model):
    name = models.CharField(max_length=5)
 
    def __str__(self):
        return self.name
 
class RequestBlood(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    state = models.CharField(max_length=200, blank=True)
    city = models.CharField(max_length=300, blank=True)
    address = models.CharField(max_length=500, blank=True)
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    date = models.CharField(max_length=100, blank=True)
 
    def __str__(self):
        return self.name
 
class Donor(models.Model):
    donor = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    date_of_birth = models.CharField(max_length=100)
    phone = models.CharField(max_length=10)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    address = models.TextField(max_length=500, default="")
    blood_group = models.ForeignKey(BloodGroup, on_delete=models.CASCADE)
    gender = models.CharField(max_length=10)
    image = models.ImageField(upload_to="")
    ready_to_donate = models.BooleanField(default=True)
 
    def __str__(self):
        return str(self.blood_group)
Code Explanation:
Blood Group model:
It saves the name of all the blood groups.
Request Blood model:
When a user or patient requests for blood by filling the required form, all the data is stored in this model.
Donor model:
When a new donor registers, all the data is stored in this model.

Advertisement
Urls.py :
urlpatterns = [
    path("", views.index, name="index"),
    path("donors_list/<int:myid>/", views.donors_list, name="donors_list"),
    path("donors_details/<int:myid>/", views.donors_details, name="donors_details"),
    path("request_blood/", views.request_blood, name="request_blood"),
    path("see_all_request/", views.see_all_request, name="see_all_request"),
    path("become_donor/", views.become_donor, name="become_donor"),
    path("login/", views.Login, name="login"),
    path("logout/", views.Logout, name="logout"),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('change_status/', views.change_status, name='change_status'),
]
Code Explanation:

Above code consists of all the urls used in the Python Blood Donation project.

1. Home Page (index.html):
<div class="container">
<h1>Available Donors According To Blood Group</h1>
  <div class="album py-5 bg-light">
    <div class="container">
      <div class="row">
        {% for i in all_group %}
        <div class="col-md-4">
          <div class="card mb-4 shadow-sm border-danger">
            <div class="card-body">
              <h3 class="card-text">Blood Group: {{i.name}}</h3>
              <h3 class="card-text">Total Donor: {{i.total}}</h3>
              <div class="d-flex justify-content-between align-items-center">
                <div class="btn-group">
                  <a href="/donors_list/{{i.id}}/" class="btn btn-sm btn-outline-danger">View All Donors</a>
                </div>
              </div>
            </div>
          </div>
        </div>
        {% endfor %}
      </div>
    </div>
  </div>
</div>
Views.py :

Advertisement
def index(request):
    all_group = BloodGroup.objects.annotate(total=Count('donor'))
    return render(request, "index.html", {'all_group':all_group})
Code Explanation:
On the home page there are bootstrap cards for each blood group with their total numbers. All the users can see the available donors for each blood group. Then the users can also see the details of all donors.

2. Request For Blood (request_blood.html):
<div class="container">
    <h3><i style="font-weight: bold;    ">Request For Blood</i></h3>
    <form method="POST"> {% csrf_token %}
<div class="row mt-4">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Full Name</i></label>
        <input type="text" class="form-control" name="name" id="name" placeholder="Enter Name" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Email ID</i></label>
        <input type="email" class="form-control" name="email" id="email" placeholder="Enter Email ID" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Contact Number</i></label>
        <input type="tel" class="form-control" name="phone" id="phone" placeholder="Enter Contact Number" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">State</i></label>
        <input type="text" class="form-control" name="state" id="state" placeholder="Enter State" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">City</i></label>
        <input type="text" class="form-control" name="city" id="city" placeholder="Enter City" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Address</i></label>
        <textarea class="form-control" id="address" name="address" rows="3" placeholder="Enter Address" required></textarea>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Blood Group</i></label>
        <select class="form-control" name="blood_group" required>
            <option>A+</option>
            <option>A-</option>
            <option>B+</option>
            <option>B-</option>
            <option>O+</option>
            <option>O-</option>
            <option>AB+</option>
            <option>AB-</option>
            </select>
    </div>
        <div class="form-group col-md-6">
            <label><i style="font-weight: bold;">Date Of Donation</i></label>
            <input type="date" class="form-control" id="date" name="date" required>
        </div>
</div>
<button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>
Views.py :

def request_blood(request):
    if request.method == "POST":
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        blood_requests = RequestBlood.objects.create(name=name, email=email, phone=phone, state=state, city=city, address=address, blood_group=BloodGroup.objects.get(name=blood_group), date=date)
        blood_requests.save()
        return render(request, "index.html")
    return render(request, "request_blood.html")
Code Explanation:
Anyone in need of blood can make a request for blood. All the blood requests will be visible to everyone. If any donor wants to help any person who has made a request, then the donor can contact the person.

Advertisement

3. All Blood Requests (see_all_request.html):
<div class="container">
{% if requests %}
<h3 class="text-center">All Blood Requests</h3>
<br>
<table class="table table-sm table-bordered">
  <tr class="table-danger">
    <th>Name</th>
    <th>Phone</th>
    <th>Email</th>
    <th>Blood Group</th>
    <th>Donation Date</th>
    <th>State | City</th>
  </tr>
  {% for i in requests %}
    <tr>
      <td>{{i.name}}</td>
      <td>{{i.phone}}</td>
      <td>{{i.email}}</td>
      <td>{{i.blood_group}}</td>
      <td>{{i.date}}</td>
      <td>{{i.state}} | {{i.city}}</td>
    </tr>
  {% endfor %}
</table>
{% else %}
<h2>No Blood Request Available</h2>
{% endif %}
</div>
Views.py :

def see_all_request(request):
    requests = RequestBlood.objects.all()
    return render(request, "see_all_request.html", {'requests':requests})
Code Explanation:
By clicking on see all requests on the navigation bar, the user can see the entire list of blood requests. Donors can contact the person in need of the blood if they want to help that person.

Advertisement

4. Become a Donor (become_donor.html):
<div class="container">
    <form method="POST" enctype="multipart/form-data"> {% csrf_token %}
<div class="row mt-1">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Username</i></label>
        <input type="text" class="form-control" name="username" id="username" placeholder="Enter Username" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">First Name</i></label>
        <input type="text" class="form-control" name="first_name" id="first_name" placeholder="Enter First Name" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Last Name</i></label>
        <input type="text" class="form-control" name="last_name" id="last_name" placeholder="Enter Last Name" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Email ID</i></label>
        <input type="email" class="form-control" name="email" id="email" placeholder="Enter Email ID" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Contact Number</i></label>
        <input type="tel" class="form-control" name="phone" id="phone" placeholder="Enter Contact Number" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">State</i></label>
        <input type="text" class="form-control" name="state" id="state" placeholder="Enter State" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">City</i></label>
        <input type="text" class="form-control" name="city" id="city" placeholder="Enter City" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Address</i></label>
        <textarea class="form-control" id="address" name="address" rows="3" placeholder="Enter Address" required></textarea>
    </div>
</div>
 
<div class="row mt-2">
<div class="form-group col-md-6">
    <label><i style="font-weight: bold;">Gender</i></label>
<div style="border: 1px solid lightgrey; padding: 5px; border-radius: 6px;">
<div class="form-check form-check-inline">
    <input class="form-check-input" type="radio" name="gender" id="male" value="Male">
    <label class="form-check-label">Male</label>
  </div>
  <div class="form-check form-check-inline">
    <input class="form-check-input" type="radio" name="gender" id="female" value="Female">
    <label class="form-check-label">Female</label>
  </div>
  </div>
  </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Blood Group</i></label>
        <select class="form-control" name="blood_group" required>
            <option>A+</option>
            <option>A-</option>
            <option>B+</option>
            <option>B-</option>
            <option>O+</option>
            <option>O-</option>
            <option>AB+</option>
            <option>AB-</option>
            </select>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Profile Photo</i></label>
        <input type="file" class="form-control" id="image" name="image" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Date Of Birth</i></label>
        <input type="date" class="form-control" id="date" name="date" required>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Password</i></label>
        <input type="password" class="form-control" name="password" id="password" placeholder="Enter Password" required>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Confirm Password</i></label>
        <input type="password" class="form-control" name="confirm_password" id="confirm_password" placeholder="Confirm Password" required>
    </div>
</div>
 
<button type="submit" class="btn btn-primary">Submit</button>
</form>
</div>
Views.py :

Advertisement

def become_donor(request):
    if request.method=="POST":   
        username = request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        date = request.POST['date']
        image = request.FILES['image']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
 
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect('/signup')
 
        user = User.objects.create_user(username=username, email=email, first_name=first_name, last_name=last_name, password=password)
        donors = Donor.objects.create(donor=user, phone=phone, state=state, city=city, address=address, gender=gender, blood_group=BloodGroup.objects.get(name=blood_group), date_of_birth=date, image=image)
        user.save()
        donors.save()
        return render(request, "index.html")
    return render(request, "become_donor.html")
Code Explanation:
All users can register themselves as donors by filling the form by clicking on register as donor option on the navigation bar. After registering themselves as a donor they can check their profile and are able to edit the profile. The donors can update the status of whether they are ready to donate blood or not.

5. Login (login.html):
Advertisement
<form method="POST"> {% csrf_token %}
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
        <input type="submit" value="Submit" class="btn btn-primary" style="color: white; font-size: larger; width: 8rem;">
    </div>
</form>
Views.py :

def Login(request):
    if request.user.is_authenticated:
        return redirect("/")
    else:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
 
            if user is not None:
                login(request, user)
                return redirect("/profile")
            else:
                thank = True
                return render(request, "user_login.html", {"thank":thank})
    return render(request, "login.html")
Code Explanation:
After registering as a donor, the donors can login using the username and password.

user = authenticate(username=username, password=password)
Using django’s authenticate function, the donors can login.

6. Donor’s Profile (profile.html):
Advertisement
<div class="container">
    <div class="row">
        <div class="col-md-4">
            <div>
                <img src="{{donor_profile.image.url}}" alt="" width="310px" height="270px">
                <br><br><br>
                {% if donor_profile.ready_to_donate %}
                <a href="/change_status/" class="btn btn-success" style="width: 15rem; font-size: 23px;">I'm Ready To Donate</a>
              {% else %}
                <a href="/change_status/" class="btn btn-danger" style="width: 15rem; font-size: 19px;">I'm Not Ready To Donate</a>
              {% endif %}
            </div>
        </div>
        <div class="col-md-8">
            <div>
                <div>
                    <br>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Username:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{user}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Full Name:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{user.get_full_name}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Email:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{user.email}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Phone Number:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.phone}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Gender</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.gender}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Date of Birth:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.date_of_birth}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>State:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.state}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>City:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.city}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Address:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.address}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Blood Group:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.blood_group}}</h3>
                        </div>
                    </div>
                    <div class="row mt-2">
                        <div class="col-md-6">
                            <h3>Address:</h3>
                        </div>
                        <div class="col-md-6">
                            <h3>{{donor_profile.address}}</h3>
                        </div>
                    </div>
                </div>
                <a href="/edit_profile/" class="btn btn-outline-danger mt-4">Edit Profile</a>
            </div>
        </div>
</div>
</div>
Views.py :

@login_required(login_url = '/login')
def profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    return render(request, "profile.html", {'donor_profile':donor_profile})
Advertisement

Code Explanation:
After login, the donor’s profile is shown to them. If they are not ready to donate blood then they can change the status from their profile that they are not ready for donating blood. Whenever a new donor registers, the default status is set to ready to donate blood in their profile.

7. Edit Profile (edit_profile.html):
<div class="container">
    <form method="POST" enctype="multipart/form-data"> {% csrf_token %}
<div class="row mt-1">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Username</i></label>
        <input type="text" class="form-control" name="username" id="username" value="{{user}}" readonly>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">First Name</i></label>
        <input type="text" class="form-control" name="first_name" id="first_name" value="{{request.user.first_name}}" readonly>
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Last Name</i></label>
        <input type="text" class="form-control" name="last_name" id="last_name" value="{{request.user.last_name}}" readonly>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Email ID</i></label>
        <input type="email" class="form-control" name="email" id="email" value="{{request.user.email}}">
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Contact Number</i></label>
        <input type="tel" class="form-control" name="phone" id="phone" value="{{donor_profile.phone}}">
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">State</i></label>
        <input type="text" class="form-control" name="state" id="state" value="{{donor_profile.state}}">
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">City</i></label>
        <input type="text" class="form-control" name="city" id="city" value="{{donor_profile.city}}">
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-12">
        <label><i style="font-weight: bold;">Address</i></label>
        <textarea class="form-control" id="address" name="address" rows="3">{{donor_profile.address}}</textarea>
    </div>
</div>
 
<div class="row mt-2">
<div class="form-group col-md-6">
    <label><i style="font-weight: bold;">Gender</i></label>
    <input type="text" class="form-control" name="gender" value="{{donor_profile.gender}}" readonly>
  </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Blood Group</i></label>
        <input type="text" class="form-control" name="blood_group" value="{{donor_profile.blood_group}}" readonly>
    </div>
</div>
 
<div class="row mt-1">
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Profile Photo</i><a href="{{donor_profile.image.url}}">Click here to view the current profile <picture></picture></a></label>
        <input type="file" class="form-control" id="image" name="image">
    </div>
    <div class="form-group col-md-6">
        <label><i style="font-weight: bold;">Date Of Birth</i></label>
        <input type="date" class="form-control" id="date" name="date" value="{{donor_profile.date_of_birth}}" readonly>
    </div>
</div>
 
<button type="submit" class="btn btn-primary">Update Profile</button>
</form>
</div>
Views.py :

@login_required(login_url = '/login')
def edit_profile(request):
    donor_profile = Donor.objects.get(donor=request.user)
    if request.method == "POST":
        email = request.POST['email']
        phone = request.POST['phone']
        state = request.POST['state']
        city = request.POST['city']
        address = request.POST['address']
 
        donor_profile.donor.email = email
        donor_profile.phone = phone
        donor_profile.state = state
        donor_profile.city = city
        donor_profile.address = address
        donor_profile.save()
        donor_profile.donor.save()
 
        try:
            image = request.FILES['image']
            donor_profile.image = image
            donor_profile.save()
        except:
            pass
        alert = True
        return render(request, "edit_profile.html", {'alert':alert})
    return render(request, "edit_profile.html", {'donor_profile':donor_profile})
Code Explanation:
Blood Donor’s can edit their profile after registering themselves whenever they want. Some information like the name, blood group cannot be edited.

Advertisement
Python Blood Donation Project Output:
Home Page:

python blood donation home

Blood Donor’s List of particular blood group:

Advertisement

blood donors list group
