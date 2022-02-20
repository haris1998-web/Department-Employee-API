from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from django.core.files.storage import default_storage
from rest_framework.response import Response

from .models import *
from .serializers import *

# Create your views here.
@csrf_exempt
def departmentAPI(request, id=0):
    if request.method == 'GET':
        departments = Department.objects.all()
        departments_serializer = DepartmentSerializer(departments, many=True)
        return JsonResponse(departments_serializer.data, safe=False)

    elif request.method == 'POST':
        department_data = JSONParser().parse(request)
        department_serializer = DepartmentSerializer(data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        department_data = JSONParser().parse(request)
        department = Department.objects.get(DepartmentID=department_data['DepartmentID'])
        department_serializer = DepartmentSerializer(department, data=department_data)
        if department_serializer.is_valid():
            department_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        department = Department.objects.get(DepartmentID=id)
        department.delete()
        return JsonResponse('Deleted Successfully', safe=False)

@csrf_exempt
def employeeAPI(request, id=0):
    if request.method == 'GET':
        employees = Employee.objects.all()
        employees_serializer = EmployeeSerializer(employees, many=True)
        return JsonResponse(employees_serializer.data, safe=False)

    elif request.method == 'POST':
        employees_data = JSONParser().parse(request)
        employees_serializer = EmployeeSerializer(data=employees_data)
        if employees_serializer.is_valid():
            employees_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to add", safe=False)

    elif request.method == 'PUT':
        employee_data = JSONParser().parse(request)
        employee = Employee.objects.get(EmployeeID=employee_data['DepartmentID'])
        employee_serializer = EmployeeSerializer(employee, data=employee_data)
        if employee_serializer.is_valid():
            employee_serializer.save()
            return JsonResponse("Updated Successfully", safe=False)
        return JsonResponse("Failed to update", safe=False)

    elif request.method == 'DELETE':
        employee = Employee.objects.get(EmployeeID=id)
        employee.delete()
        return JsonResponse('Deleted Successfully', safe=False)


@csrf_exempt
def saveFile(request):
    file = request.FILES['myFile']
    file_name = default_storage.save(file.name, file)

    return JsonResponse(file_name, safe=False)
