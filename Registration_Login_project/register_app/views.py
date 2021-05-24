from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth

# Create your views here.
def Index(request):
    return render(request,'index.html')

def Register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['cnfpswd']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,"User name already exit")
                return redirect('Register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exits")
                return redirect('Register')
            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()
                return redirect('Login')
        else:
            messages.info(request,"password not matching")
            return redirect('Register')
        return redirect('/')

    return render(request,'registration.html')

def Login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'please enter correct credentials')
            return redirect('Login')
    return render(request,'login.html')

def Logout(request):
    auth.logout(request)
    return redirect('/')