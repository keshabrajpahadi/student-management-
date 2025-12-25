from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import Student
from .forms import StudentForm
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def show(request):
    stu=Student.objects.all()
    context={
        'stu':stu
    }
    return render(request,'student_manage/show.html',context)

def update_student(request,pk):
    stu = get_object_or_404(Student, id=pk)
    if request.method == "POST":
        stu=Student.objects.get(id=pk)
        form=StudentForm(request.POST,instance=stu)
        if form.is_valid():
         form.save()
         return redirect('home')    
    form=StudentForm(instance=stu)
    context={
        'stu':stu,
        'form':form
    }
    return render(request, 'student_manage/update_student.html',context)



def delete_student(request,pk):
    if request.method == "POST":
        stu=Student.objects.get(id=pk)
        stu.delete()
        return redirect('home')


def add_student(request):
   
    if request.method == "POST":
         form=StudentForm(request.POST)
         if form.is_valid():
          form.save()
          return redirect('home')
    form=StudentForm()
    context={
        'form':form
    }
    return render(request,'student_manage/add_student.html',context)

def search_student(request):
   if request.method =="POST":
      search=request.POST.get("output")
      std=Student.objects.all()
      if search:
         stu=std.filter(Q(fname__icontains=search)|
                            Q(lname__icontains=search)|
                            Q(email__icontains=search)|
                            Q(branch__icontains=search))
         context={
            'stu':stu
         }
         return render(request,'student_manage/list_student.html',context)
      return HttpResponse("error occureed")
def home(request):
   return render(request,'student_manage/home.html')

def signup_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {
        'form': form
    }
    return render(request, 'student_manage/signup.html', context)