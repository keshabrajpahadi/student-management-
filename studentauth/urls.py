from django.urls import path
from .views import home,signup_user,logout_user,login_user

urlpatterns = [
    path('',home,name='home'),
     path('signup/',signup_user,name='signup'),
       path('logout/',logout_user,name='logout'),
        path('login/',login_user,name='login')

]