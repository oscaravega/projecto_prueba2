from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'companies', views.CompanyViewSet)
router.register(r'employees', views.EmployeeViewSet)
router.register(r'attendances', views.AttendanceViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('create-attendance/', views.create_attendance, name='create-attendance'),
    path('delete-company/<int:pk>/', views.delete_company, name='delete-company'),
    path('delete-employee/<int:pk>/', views.delete_employee, name='delete-employee'),
]