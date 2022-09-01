from rest_framework.serializers import ModelSerializer
from .models import *


class RestaurantSerializer(ModelSerializer):
    class Meta:
        model = Restaurant
        fields = '__all__'


class EmployeeSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'password')


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = Employee
        fields = ('id', 'username', 'email', 'password', 'first_name', 'last_name')
        extra_kwargs = {
            'password': {'write_only': True},
        }

    def create(self, validated_data):
        employee = Employee.objects.create_user(username=validated_data['username'],
                                                email=validated_data['email'],
                                                password=validated_data['password'],
                                                first_name=validated_data['first_name'],
                                                last_name=validated_data['last_name'])
        return employee


class MenuSerializer(ModelSerializer):
    class Meta:
        model = Menu
        fields = '__all__'
