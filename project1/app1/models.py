from django.db import models

# Create your models here.

class Student_Model(models.Model):
    student_id = models.IntegerField(primary_key=True)
    student_fname = models.CharField(max_length=30)
    student_lname = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    grade = models.IntegerField()

    def __str__(self):
        return f'{self.student_id}-{self.student_fname}'
    
    