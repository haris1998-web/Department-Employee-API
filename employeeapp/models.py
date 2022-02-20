from operator import mod
from pyexpat import model
from django.db import models

# Create your models here.


class Department(models.Model):
    DepartmentID = models.AutoField(primary_key=True)
    DepartmentName = models.CharField(max_length=100)

    def __str__(self):
        return self.DepartmentName


class Employee(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    EmployeeName = models.CharField(max_length=100)
    Department = models.CharField(max_length=100)
    DateofJoining = models.DateField(auto_now=True)
    PhotoFileName = models.CharField(max_length=100)

    def __str__(self):
        return self.EmployeeName