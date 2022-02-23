from django.shortcuts import render,redirect
from django.contrib.auth.models import User

# Create your views here.
def signup(request):
    if request.method =='POST':
        username=request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        x=User.objects.create_user(username=username,first_name=firstname,last_name=lastname,email=email,password=password)
        x.save()
        print("user created")
        return redirect('/')


    return render(request,'b.html')