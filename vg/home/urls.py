from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name="home"),
    path('student', views.student, name="student"),
    path('guru', views.guru, name = 'guru'),
    path('loginguru', views.loginguru, name="loginguru"),
    path('registerguru', views.registerguru, name="registerguru"),
    path('gurulogin', views.gurulogin, name="gurulogin"),
    path('gururegister', views.gururegister, name="gururegister"),
    path('resume', views.resume, name="resume"),
    path('home/resumecss', views.resumecss, name="resumecss"),
    path('studentlogin', views.studentlogin, name="studentlogin"),
    path('login', views.login, name="login"),
    path('register', views.register, name="register"),
    path('loginstudent', views.loginstudent, name="loginstudent"),
    path('registerstudent', views.registerstudent, name="registerstudent"),
    path('details', views.details, name='details'),
    path('api/studentdetailsview', views.studentdetailsview, name = 'StudentDetailsViewSet'),
    path('api/gurudetailsview', views.gurudetailsview, name = 'GuruDetailsViewSet'),
    path('api/createstudent', views.createstudent, name = 'StudentDetailsViewSet'),
    path('api/createguru', views.createguru, name = 'GuruDetailsViewSet')
]