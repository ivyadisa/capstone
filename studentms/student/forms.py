from django import forms
from .models import Student, Teacher, Class, Fee

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['admission_number', 'first_name', 'last_name', 'dob', 'gender', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'admission_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
# teacher form
class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['staff_number', 'first_name', 'last_name', 'dob', 'gender', 'address']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gender': forms.Select(attrs={'class': 'form-select'}),
            'staff_number': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

# class form
class ClassForm(forms.ModelForm):
    class Meta:
        model = Class
        fields = ['name', 'teacher']

# Fee form

class FeeForm(forms.ModelForm):
    class Meta:
        model = Fee
        fields = ['student', 'term', 'amount_due', 'amount_paid', 'payment_date']
        widgets = {
            'student': forms.Select(attrs={'class': 'form-select'}),
            'term': forms.TextInput(attrs={'class': 'form-control'}),
            'amount_due': forms.NumberInput(attrs={'class': 'form-control'}),
            'amount_paid': forms.NumberInput(attrs={'class': 'form-control'}),
            'payment_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

