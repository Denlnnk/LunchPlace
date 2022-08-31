from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .service.restaurant_upload_service import upload


# Create your views here.
@api_view(['GET'])
def getRoutes(request):
    routes = [
        'POST /upload_system/',
        'POST /create_employee/',
        'GET /view_menu/<str:restaurant_name>/',
        'GET /view_restaurants/',
    ]

    return Response(routes)


@api_view(['GET'])
def get_restaurant(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def get_employee(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def view_menu(request, restaurant_name):
    menu = Menu.objects.filter(restaurant_name__icontains=restaurant_name)
    serializer = MenuSerializer(menu, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def create_restaurant(request):
    serializer = RestaurantSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def vote_restaurant(reqeust, restaurant_name):
    Restaurant.objects.filter(title__icontains=restaurant_name).update(vote=F('vote') + 1)


@api_view(['POST'])
def create_employee(request):
    serializer = EmployeeSerializer(data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def upload_system(request):
    if 'day' not in request.data.keys():
        raise Exception('Expected day parameter in request body')

    Restaurant.objects.all().delete()
    Menu.objects.all().delete()

    restaurant_info_list = upload(request.data)
    for restaurant_info in restaurant_info_list:
        restaurant_serializer = RestaurantSerializer(data={'title': restaurant_info['name'],
                                                           'description': restaurant_info['description'],
                                                           'phone_number': restaurant_info['phone_number']})
        if restaurant_serializer.is_valid():
            restaurant_serializer.save()

        for dish in restaurant_info['menu']:
            serializer = MenuSerializer(data={'name': dish['name'],
                                              'price': dish['price'],
                                              'restaurant_name': restaurant_info['name']})

            if serializer.is_valid():
                serializer.save()

    return Response(True)
