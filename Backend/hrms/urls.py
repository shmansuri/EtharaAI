from django.urls import path
from .views import (
    EmployeeListCreateView,
    EmployeeDeleteView,
    AttendanceCreateView,
    AttendanceByEmployeeAPIView,
)

urlpatterns = [
    # Employee endpoints
    path("employees/", EmployeeListCreateView.as_view(), name="employee-list-create"),
    path("employees/<int:pk>/", EmployeeDeleteView.as_view(), name="employee-delete"),

    # Attendance endpoints
    path("attendance/", AttendanceCreateView.as_view(), name="attendance-create"),
    path("attendance/<str:emp_identifier>/", AttendanceByEmployeeAPIView.as_view())


]
