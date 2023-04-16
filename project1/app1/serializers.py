from rest_framework import serializers
from .models import Student_Model

class Student_Model_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Student_Model
        fields = ['student_id', 'student_fname', 'student_lname', 'address', 'grade']