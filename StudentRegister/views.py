from django.db.models.signals import post_save
from django.dispatch import receiver
from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .models import Student
from .forms import StudentForm
from django.http import HttpResponse 
from django.core import serializers
import requests
import json
import datetime
# Create your views here.
from django.shortcuts import render
from django.db import connection

def showFiltered(request):

    students = Student.objects.filter(send=0)
    context = {'students': students}
    for student in students:
        student.send = 1
        student.save()
    json_data = serializers.serialize('json', students)
    pour_json = serializers.serialize('json', students)
    client_ip = request.META.get('REMOTE_ADDR')
    current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    modified_data = str(json_data).replace("\\", " ")
    with open('output'+current_datetime+'.json', 'w', encoding='utf-8') as json_file:
        json_file.write(modified_data)
    return HttpResponse(pour_json)

def show(request):
    students =Student.objects.all()
    context = {'students': students}
    
    json_data = serializers.serialize('json', students)
    modified_data = str(json_data).replace("\\", " ")
    with open('output.json', 'w', encoding='utf-8') as json_file:
        json_file.write(modified_data)
        
    return HttpResponse(json_data)
   
def Add_Info(request):
    students = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        context = {'has_error': False}
        Admission_Number = request.POST.get('Admission_Number')
        First_Name = request.POST.get('First_Name')
        Last_Name = request.POST.get('Last_Name')
        Date_Of_Birth = request.POST.get('Date_Of_Birth')
        Date_Joined = request.POST.get('Date_Joined')
        Faculty = request.POST.get('Faculty')
        Department = request.POST.get('Department')
        Course_Name = request.POST.get('Course_Name')
        Year_Of_Study = request.POST.get('Year_Of_Study')
        Unit_Name = request.POST.get('Unit_Name')
        Grade = request.POST.get('Grade')
        send = 0

        student = Student.objects.create(Admission_Number=Admission_Number, First_Name=First_Name, Last_Name=Last_Name,
        Date_Of_Birth=Date_Of_Birth, Date_Joined=Date_Joined, Faculty=Faculty, Department=Department, 
        Course_Name=Course_Name, Year_Of_Study=Year_Of_Study, Unit_Name=Unit_Name, Grade=Grade,send = 0).save()

        if not context['has_error']:
            messages.success(request, '✅ Student Info Successfully Added!')
            return redirect('Add_Info')
        
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Added!')
            return redirect('Add_Info')
    context = {'students': students, 'form': form}  
    # print(students)
    
    return render(request, 'Index.html', context)

def View_Info(request, id):
    student = Student.objects.get(id=id)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
    else:
        form = StudentForm(instance=student)

    context = {'student': student, 'form':form}

    return render(request, 'View.html', context)

def Edit_Info(request, id):
    student = Student.objects.get(id=id)

    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, '✅ Student Info Successfully Updated!')
            return redirect('Add_Info')
        else:
            messages.error(request, '⚠️ Student Info Unsuccessfully Updated!')
            return redirect('Add_Info')
    else:
        form = StudentForm(instance=student)
    
    context = {'student':student, 'form':form} 
    return render(request, 'Edit.html', context)
    

def Delete_Info(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    

    return redirect('Add_Info')
