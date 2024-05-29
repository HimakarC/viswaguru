from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse, response
from .models import studentdetails, gurudetails

# Create your views here.

def home(request):
    return render(request, "home.html")

def student(request):
    return render(request, 'student.html')

def guru(request):
    return render(request, 'guru.html')

def loginguru(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['Password']
        re = gurudetails.objects.filter(username=username, password=password).exists()
        if re:
            return redirect('details')
        else:
            messages.info(request, "User doesn't exists.")
            return redirect("gururegister")

def registerguru(request):
    if request.method == 'POST':
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        username = request.POST['user']
        password = request.POST['Password']
        gmail = request.POST['Email']
        user = gurudetails(username=username, password=password, firstname = firstname, lastname = lastname, gmail = gmail)
        re = gurudetails.objects.filter(username=username, password=password).exists()
        if re:
            messages.info(request, "User already exists.")
            return render(request, 'gurulogin.html')
        else:
            messages.info(request, "User added successfully.")
            user.save()
            return redirect('gurulogin')

def gurulogin(request):
    return render(request, 'gurulogin.html')

def gururegister(request):
    return render(request, 'gururegister.html')

def details(request):
    return render(request, 'gurudetails.html')

def resume(request):
    return render(request, 'resume.html')

def resumecss(request):
    return render(request, 'resumecss.css')

def loginstudent(request):
    if request.method == 'POST':
        username = request.POST['user']
        password = request.POST['Password']
        re = studentdetails.objects.filter(username=username, password=password).exists()
        if re:
            return redirect('studentlogin')
        else:
            messages.info(request, "User doesn't exists.")
            return redirect("register")

def registerstudent(request):
    if request.method == 'POST':
        firstname = request.POST['Firstname']
        lastname = request.POST['Lastname']
        username = request.POST['user']
        password = request.POST['Password']
        gmail = request.POST['Email']
        user = studentdetails(username=username, password=password, firstname = firstname, lastname = lastname, gmail = gmail)
        re = studentdetails.objects.filter(username=username, password=password).exists()
        if re:
            messages.info(request, "User already exists.")
            return render(request, 'login.html')
        else:
            messages.info(request, "User added successfully.")
            user.save()
            return redirect('login')

def studentlogin(request):
    return render(request, "studentmain.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")