from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=4)
    User = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(User.username)