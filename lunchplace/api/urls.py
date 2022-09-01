from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .api import EmployeeAPIView
from . import views

urlpatterns = [
    path('', views.get_routes),
    path('employee/', EmployeeAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('view_restaurants/', views.view_restaurants),
    path('vote/<str:restaurant_name>/', views.vote_restaurant),
    path('view_employees/', views.view_employees),
    path('register_employee/', views.create_employee),
    path('view_menu/<str:restaurant_name>/', views.view_menu),
    path('upload_system/', views.upload_system),
]
