from django.urls import path
from .views import home_page,login_page,signup_page,logout_user
urlpatterns = [
    path('',home_page,name='index'),
    path('login/',login_page,name='login'),
    path('logout/',logout_user,name='logout'),
    path('signup/',signup_page,name='signup'),
]


app_name = 'users'