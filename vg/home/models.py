from django.db import models
from rest_framework import serializers, viewsets
from rest_framework.routers import DefaultRouter
from django.urls import path, include

class studentdetails(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 500)
    password = models.CharField(max_length = 32)
    gmail = models.EmailField(max_length = 100)

class gurudetails(models.Model):
    firstname = models.CharField(max_length = 100)
    lastname = models.CharField(max_length = 100)
    username = models.CharField(max_length = 500)
    password = models.CharField(max_length = 32)
    gmail = models.EmailField(max_length = 100)
