# Ex02 Django ORM Web Application
## Date: 14-11-2024

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM

![386234081-4632f57c-a2bd-4dff-ad56-f0f421f2d3a3](https://github.com/user-attachments/assets/6bda2239-e40b-4aaf-806a-5dc08715bb7b)


## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
models.py
from django.db import models
from django.contrib import admin  
class Bank(models.Model):
        Name=models.charField(max_length=10)
        Accno=models.IntegerField(primary_key="Accno")
        Amount=models.Integerfield()
        Interest=models.FloatField()
        DoB=models.DateField()
        Aadharno=models.IntegerField()
        Email=Models.EmailField()
class BankAdmin(admin.ModelAdmin):
        list_display=('Name','Accno','Amount','Interest','DoB','Aadharno','Email')

admin.py

from django.contrib import admin
from .models importBank,BankAdmin
admin.site.register(Bank,BankAdmin)
```
## OUTPUT

![Screenshot (8)](https://github.com/user-attachments/assets/dea29a71-dbf6-47d7-b42b-f1db555fca73)

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
