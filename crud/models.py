from django.db import models

# Create your models here.
class student(models.Model):
    rollno= models.CharField(max_length=10)
    name = models.CharField(max_length=50)
    branch = models.CharField(max_length=25)
    email = models.CharField(max_length=50)
    phone = models.CharField(max_length=16)
    
    
    class Meta:
        db_table = "student"
