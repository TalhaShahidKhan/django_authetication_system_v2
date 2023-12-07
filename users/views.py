from django.shortcuts import render,HttpResponse

# Create your views here.



def home_page(request):
    return render(request,'index.html')


def login_page(requset):
    return HttpResponse("login page")

def signup_page(requset):
    return HttpResponse("Signup page")