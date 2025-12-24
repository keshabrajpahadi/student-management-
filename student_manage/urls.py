from django.urls import path
from .views import list_student,update_student,delete_student,add_student,search_student

urlpatterns = [
    path('',list_student,name='home'),
     path('update/<int:pk>/',update_student,name='update'),
      path('delete/<int:pk>/',delete_student,name='delete'),

      path('add/',add_student,name='add'),

      path('search/',search_student,name='search_student'),
     
]