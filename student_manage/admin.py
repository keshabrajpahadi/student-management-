from django.contrib import admin
from .models import Student

# Register your models here.
@admin.register(Student)

class StudentAdmin(admin.ModelAdmin):
    list_display=["fname","lname","email","phone","branch"]
  #list_display=[fields.name for fields in STudent._meta.get_fields()]