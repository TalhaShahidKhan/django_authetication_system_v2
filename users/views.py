from django.forms import ValidationError
from django.shortcuts import render,redirect
from django.contrib.auth import  logout,login, authenticate
from django.contrib.auth import get_user_model
from django.contrib import messages

# Create your views here.

User = get_user_model()


def home_page(request):
    return render(request,'index.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username = username,password = password)
        if user is not None:
            login(request, user)
            return redirect("/")
        
    return render(request, 'login.html')

def signup_page(request):
    error_messages = {"password_mismatch": ("The two password fields didn’t match."),"username_exist":("This username already exist")}
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        password_check = False if password1 and password2 and password1 != password2 else True
        username_check = False if (username and User.objects.filter(username__iexact=username).exists()) else True
        print(password_check,username_check)
        if password_check != True or username_check != True:
            messages.error(request, "This username already exists or The passwords Mismatched!!")
        else:
            user = User.objects.create(first_name = first_name,last_name = last_name,username = username,email = email,password = password1)
            user.set_password(user.password)
            user.save()
            return redirect('/login')
    return render(request,'signup.html')


def logout_user(request):
    logout(request)
    return redirect("/")