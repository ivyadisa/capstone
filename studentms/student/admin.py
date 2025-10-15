from django.contrib import admin
from .models import Student , Teacher ,Fee , Class
 
# Register your models here.
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("admission_number", "first_name", "last_name", "gender", "dob")
    search_fields = ("admission_number", "first_name", "last_name")

@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("staff_number", "first_name", "last_name", "gender", "dob")
    search_fields = ("staff_number", "first_name", "last_name")

@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ("name", "teacher")
    search_fields = ("name", "teacher__first_name", "teacher__last_name")
    list_filter = ("teacher",)
    ordering = ("name",)

@admin.register(Fee)
class FeeAdmin(admin.ModelAdmin):
    list_display = ('student', 'term', 'amount_due', 'amount_paid', 'balance', 'payment_status')
    list_filter = ('term', 'payment_status')
    search_fields = ('student__first_name', 'student__last_name')

