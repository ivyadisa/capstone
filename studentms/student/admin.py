from django.contrib import admin
from .models import Student , Teacher

# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("admission_number", "first_name", "last_name", "gender", "dob")
    search_fields = ("admission_number", "first_name", "last_name")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("staff_number", "first_name", "last_name", "gender", "dob")
    search_fields = ("staff_number", "first_name", "last_name")

