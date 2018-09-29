
from django.shortcuts import render,redirect
from .models import StudentInfo
from .forms import AddStudentForm


def add_studen(request):
    if request.method =='POST':
        form = AddStudentForm(request.POST)
        if form.is_valid():
            form.save()
    form = AddStudentForm()
    contxt = {'forms':form}
    return render (request,'student/add_student.html',contxt)


def all_students(request):
    std_list = StudentInfo.objects.all()
    contex = {'all_student':std_list}
    return render (request,'student/std_list.html',contex)


def delete_std(request,id):
    select = StudentInfo.objects.get(id=id)
    select.delete()
    return redirect('student_list_urls')
