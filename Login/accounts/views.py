from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.shortcuts import render, redirect

# Create your views here.
def register(request):
    if request.method == 'POST':
        name = request.POST['name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                print('Email is already taken')
            else:
                user = User.objects.create_user(email=email, password=password, first_name=name, last_name=last_name)
                user.save()
                print('User created')
                return redirect('login')
        else:
            messages.info(request, 'Both passwords are not matching')
            return redirect(register)
    else:
        return render(request, 'register.html')
    
def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        user = auth.authenticate(email=email, password=password)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('login')
    else:
        return render(request, 'login.html')
    
def home(request):
    return render(request, 'home.html')