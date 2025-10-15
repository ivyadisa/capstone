from django.shortcuts import render, redirect
from .models import Student, Teacher, Class, Fee
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import StudentForm, TeacherForm, ClassForm, FeeForm
from django.shortcuts import get_object_or_404
from rest_framework import generics
from .serializers import StudentSerializer, TeacherSerializer, ClassSerializer, FeeSerializer


# Create your views here.



def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully! Please log in.")
            return redirect('login')
        else:
            messages.error(request, "Please correct the errors below.")
    else:
        form = UserCreationForm()

    return render(request, 'registration/signup.html', {'form': form})


def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard')
        messages.error(request, "Invalid username or password.")
    else:
        form = AuthenticationForm()

    return render(request, 'registration/login.html', {'form': form})
def logout_view(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'dashboard.html')


def student_list(request):
    students = Student.objects.all()
    return render(request, 'student/student_list.html', {'students': students})

@login_required(login_url='login')
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, 'student/student_detail.html', {'student': student})

@login_required(login_url='login')
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student added successfully.")
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student/student_form.html', {'form': form, 'title': 'Add Student'})

@login_required(login_url='login')
def student_update(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, "Student updated successfully.")
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'student/student_form.html', {'form': form, 'title': 'Edit Student'})

@login_required(login_url='login')
def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.delete()
        messages.success(request, "Student deleted successfully.")
        return redirect('student_list')
    return render(request, 'student/student_confirm_delete.html', {'student': student})

class StudentListCreateAPI(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

class StudentRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


# Teachers Views
def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'student/teacher_list.html', {'teachers': teachers})

def teacher_detail(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    return render(request, 'student/teacher_detail.html', {'teacher': teacher})

def teacher_create(request):
    if request.method == "POST":
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'student/teacher_form.html', {'form': form})

def teacher_update(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_detail', pk=teacher.pk)
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'student/teacher_form.html', {'form': form})

def teacher_delete(request, pk):
    teacher = get_object_or_404(Teacher, pk=pk)
    if request.method == "POST":
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'student/teacher_confirm_delete.html', {'teacher': teacher})

class TeacherListCreateAPI(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class TeacherRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

    # classes
def class_list(request):
    classes = Class.objects.all()
    return render(request, 'student/class_list.html', {'classes':classes})

def class_detail(request, pk):
    class_obj = get_object_or_404(Class, pk=pk)
    return render (request, 'student/class_detail.html', {'class_obj': class_obj})

def class_create(request):
    if request.method == "POST":
        form = ClassForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('class_list')
    else:
        form = ClassForm()
    return render (request, 'student/class_form.html', {'form':form})

def class_update(request, pk):
    class_obj = get_object_or_404(Class, pk=pk )
    if request.method == "POST":
        form = ClassForm(request.POST, instance= class_obj)
        if form.is_valid():
            form.save()
            return redirect('class_detail', pk=class_obj.pk)
    else:
        form = ClassForm(instance= class_obj)
    return render( request, 'student/class_form.html', {'form': form})

def class_delete(request, pk):
    class_obj= get_object_or_404(Class, pk )
    if request.method == "POST":
        class_obj.delete()
        return redirect('class_list')
    
    return render(request, 'student/class_confirm_delete.html', {'class_obj': class_obj})

class ClassListCreateAPI(generics.ListCreateAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

class ClassRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer

# FEES MODULE VIEWS

@login_required(login_url='login')
def fee_list(request):
    fees = Fee.objects.select_related('student').all()
    return render(request, 'student/fee_list.html', {'fees': fees})


@login_required(login_url='login')
def fee_detail(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    return render(request, 'student/fee_detail.html', {'fee': fee})


@login_required(login_url='login')
def fee_create(request):
    if request.method == 'POST':
        form = FeeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Fee record added successfully.")
            return redirect('fee_list')
    else:
        form = FeeForm()
    return render(request, 'student/fee_form.html', {'form': form, 'title': 'Add Fee Record'})


@login_required(login_url='login')
def fee_update(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        form = FeeForm(request.POST, instance=fee)
        if form.is_valid():
            form.save()
            messages.success(request, "Fee record updated successfully.")
            return redirect('fee_list')
    else:
        form = FeeForm(instance=fee)
    return render(request, 'student/fee_form.html', {'form': form, 'title': 'Edit Fee Record'})


@login_required(login_url='login')
def fee_delete(request, pk):
    fee = get_object_or_404(Fee, pk=pk)
    if request.method == 'POST':
        fee.delete()
        messages.success(request, "Fee record deleted successfully.")
        return redirect('fee_list')
    return render(request, 'student/fee_confirm_delete.html', {'fee': fee})


# DRF API Views
class FeeListCreateAPI(generics.ListCreateAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer


class FeeRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView):
    queryset = Fee.objects.all()
    serializer_class = FeeSerializer






