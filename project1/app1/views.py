from django.shortcuts import render
from .models  import Student_Model
from .serializers import Student_Model_Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import  HttpResponse
from rest_framework import status

# Create your views here.

# class based view to create and list from database
class StudentView(APIView):
    
    # function to get the data from the database
    def get(self, request):
        student = Student_Model.objects.all()
        serializer = Student_Model_Serializer(student, many=True)
        return Response(serializer.data)
    
    #function to post oject to the database table
    def post(self, request):
        #JSON object will get converted to python object
        serializer = Student_Model_Serializer(data = request.data)
        print(serializer)
        #if serializer is valid then only it will get saved
        if serializer.is_valid():
            serializer.save()
            #After saving the python object send Response consisting the serialzier data
            return Response(serializer.data)
        #if serializer is invalid send errors in form of status
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Class view to update the existing object
class StudentUpdateView(APIView):
    
    def put(self, request, pk):
        student = Student_Model.objects.get(student_id = pk)
        #print(student)
        serializer = Student_Model_Serializer(student, data=request.data)
        print(serializer)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return HttpResponse("error occured")
    
    def patch(self, request, pk):
        print("inside patch function")
        student = Student_Model.objects.get(student_id = pk)
        serializer = Student_Model_Serializer(student, data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self ,request, pk):
        student = Student_Model.objects.get(student_id =pk)
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


