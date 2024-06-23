
from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import render,redirect,get_object_or_404
from .models import *

class Class(models.Model):
    name = models.CharField(max_length=255)  # E.g., "Java Class"
    description = models.TextField(blank=True, null=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    
    
    
