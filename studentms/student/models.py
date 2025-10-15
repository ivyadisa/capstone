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

class Fee(models.Model):
    PAYMENT_STATUS_CHOICES = [
        ('Paid', 'Paid'),
        ('Pending', 'Pending'),
        ('Partial', 'Partial'),
    ]

    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='fees')
    term = models.CharField(max_length=50)  
    amount_due = models.DecimalField(max_digits=10, decimal_places=2)
    amount_paid = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    balance = models.DecimalField(max_digits=10, decimal_places=2, editable=False, default=0)
    payment_status = models.CharField(max_length=10, choices=PAYMENT_STATUS_CHOICES, default='Pending')
    payment_date = models.DateField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.balance = self.amount_due - self.amount_paid
        if self.balance == 0:
            self.payment_status = 'Paid'
        elif self.amount_paid > 0 and self.balance > 0:
            self.payment_status = 'Partial'
        else:
            self.payment_status = 'Pending'
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.first_name} {self.student.last_name} - {self.term}"

