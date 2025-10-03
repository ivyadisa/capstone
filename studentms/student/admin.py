from django.contrib import admin
from .models import Student 

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("admission_number", "first_name", "last_name", "gender", "dob")
    search_fields = ("admission_number", "first_name", "last_name")


