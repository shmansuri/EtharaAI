from rest_framework import generics, status
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from rest_framework.response import Response
from django.db import IntegrityError
from .models import Employee, Attendance
from .serializers import EmployeeSerializer, AttendanceSerializer

@method_decorator(csrf_exempt, name='dispatch')
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "Employee with this email or employee ID already exists."},
                status=status.HTTP_400_BAD_REQUEST
            )


class EmployeeDeleteView(generics.DestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def create(self, request, *args, **kwargs):
        print("REQUEST DATA:", request.data)
        return super().create(request, *args, **kwargs)


@method_decorator(csrf_exempt, name='dispatch')
class AttendanceCreateView(generics.CreateAPIView):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        try:
            return super().create(request, *args, **kwargs)
        except IntegrityError:
            return Response(
                {"error": "Attendance record could not be created."},
                status=status.HTTP_400_BAD_REQUEST
            )

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Attendance

class AttendanceByEmployeeAPIView(APIView):

    def get(self, request, emp_identifier):
        # If numeric → use primary key
        if emp_identifier.isdigit():
            records = Attendance.objects.filter(
                employee_id=int(emp_identifier)
            )
        else:
            # If string → use employee_id field
            records = Attendance.objects.filter(
                employee__employee_id=emp_identifier
            )

        serializer = AttendanceSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

