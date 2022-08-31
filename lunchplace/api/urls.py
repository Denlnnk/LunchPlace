from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .serializers import UserAPIView
from . import views

urlpatterns = [
    path('', views.getRoutes),
    path('user/', UserAPIView.as_view()),

    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),

    path('view_restaurants/', views.get_restaurant),
    path('create_restaurant/', views.create_restaurant),
    path('vote/<str:restaurant_name>/', views.vote_restaurant),
    path('view_employees/', views.get_employee),
    path('create_employee/', views.create_employee),
    path('view_menu/<str:restaurant_name>/', views.view_menu),
    path('upload_system/', views.upload_system),
]
