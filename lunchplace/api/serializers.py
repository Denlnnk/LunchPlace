from rest_framework.serializers import ModelSerializer
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated
from .models import *


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'password')


class UserAPIView(RetrieveAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = EmployeeSerializer

    def get_object(self):
        return self.request.user


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
