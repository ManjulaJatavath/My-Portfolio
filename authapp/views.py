from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout
from django.contrib import messages
# Create your views here.
def signup(request):
    if request.method=="POST":
        email = request.POST.get('email')  
        password = request.POST.get('pass1')
        confirm_password = request.POST.get('pass2')
        if password!=confirm_password:
            messages.info(request,'Password is not macthing')
            return redirect('/auth/signup/')
        
        try:
            if User.objects.get(username=email):
                messages.warning(request,'Email is already exist')
        except Exception as identifier:
            pass
        user=User.objects.create_user(username=email,email=email,password=password)
        user.save()
        #
        if user is not None:
            login(request,user)
            messages.success(request,"User Created & Login Success")
            return redirect('/')
        
        # messages.success(request,'User is Created, please login')
        # return redirect('/auth/login/') 
          
    return render(request,'signup.html')

def login_view(request):
    if request.method == "POST":
        email = request.POST.get('email')  
        password = request.POST.get('password')
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful')
            return redirect('/')  # Redirect to the home page after login
        else:
            messages.error(request, 'Invalid email or password')
    return render(request, 'login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'Logged out successfully')
    return render(request, 'login.html')
