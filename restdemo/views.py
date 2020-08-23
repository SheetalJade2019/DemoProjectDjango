from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from restdemo.models import Employee
from restdemo.serializers import EmployeeSerializers

class EmployeeList(APIView):
    def get(self,request):#read or take data
        emp = Employee.objects.all()
        serializer = EmployeeSerializers(emp, many=True)
        return Response(serializer.data)
    def post():# submit data
        pass
