from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . models import employees
from . serializers import employeesSerializer


class employeeList(APIView):

    def get(self, request):  # reading taking data
        employees1 = employees.objects.all()
        # ((employees--> object, many = true)-MANY OBJECT)
        serializer = employeesSerializer(employees1, many=True)
        return Response(serializer.data)

    def post(self):  # submitting all data
        pass
