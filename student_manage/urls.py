from django.urls import path
from .views import show,signup_user,update_student,delete_student,add_student,search_student

urlpatterns = [
    path('show',show,name='show'),
    # path('',list_student,name='home'),
    #path('show/',show,name='show'),
     path('update/<int:pk>/',update_student,name='update'),
      path('delete/<int:pk>/',delete_student,name='delete'),

      path('add/',add_student,name='add'),

      path('search/',search_student,name='search_student'),
      path('signup/',signup_user,name='signup')
     
]