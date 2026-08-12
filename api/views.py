from rest_framework.decorators import action
from django.shortcuts import render
from requests import Response
from rest_framework import viewsets
from api.models import Company, Employee
from api.serilizers import CompanySerliaizer, EmployeeSerliaizer
from rest_framework.response import Response


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerliaizer

    @action(detail=True, methods=['get'])
    def employee(self,request,pk=None):
        try:
            company = Company.objects.get(pk=pk)
            empsloyees = Employee.objects.filter(Company=company)
            emps_serializer = EmployeeSerliaizer(empsloyees, many=True,context={'request': request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({"error": "Company not found"}, status=404)


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerliaizer 
