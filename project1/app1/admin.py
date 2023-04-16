from django.contrib import admin
from .models import Student_Model
# Register your models here.

@admin.register(Student_Model)
class Student_Admin(admin.ModelAdmin):
    model =  Student_Model
    list_display = ['student_id', 'student_fname', 'student_lname', 'address', 'grade']
