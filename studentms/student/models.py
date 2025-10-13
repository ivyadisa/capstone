from django.db import models
# Create your models here.

class Student(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    admission_number = models.CharField( max_length = 20, unique= True)
    first_name = models.CharField(max_length= 100 )
    last_name = models.CharField(max_length= 100 )
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices= GENDER_CHOICES )
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.admission_number})"


class Teacher(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    staff_number = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    address = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.staff_number})"


class Class(models.Model):
    name = models.CharField(max_length=50, unique=True)  
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True, related_name="classes")

    def __str__(self):
        return self.name
