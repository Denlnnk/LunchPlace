from django.db.models import F
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from .service import restaurant_upload_service
from .response import Response as res


# Create your views here.
@api_view(['GET'])
def get_routes(request):
    routes = [
        'POST /upload_system/',
        'POST /register_employee/',
        'POST /vote/<str:restaurant_name>/',
        'GET /view_employees/',
        'GET /view_restaurants/',
        'GET /view_current_day_menu/<str:restaurant_name>/',
        'GET /votes_for_day/',

    ]

    return Response(routes)


@api_view(['GET'])
def view_restaurants(request):
    restaurants = Restaurant.objects.all()
    serializer = RestaurantSerializer(restaurants, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def view_employees(request):
    employees = Employee.objects.all()
    serializer = EmployeeSerializer(employees, many=True)

    return Response(serializer.data)


@api_view(['GET'])
def view_menu(request, restaurant_name):
    menu = Menu.objects.filter(restaurant_name__icontains=restaurant_name)
    serializer = MenuSerializer(menu, many=True)

    return Response(serializer.data)


@api_view(['POST'])
def vote_restaurant(reqeust, restaurant_name):
    Restaurant.objects.filter(title__icontains=restaurant_name).update(vote=F('vote') + 1)
    return Response(True)


@api_view(['POST'])
def create_employee(request):
    serializer = RegisterSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return Response({
        "message": "User Created Successfully.  Now perform Login to get your token",
    })


@api_view(['POST'])
def upload_system(request):
    """Uploading info about Restaurants from files"""
    if 'day' not in request.data.keys():
        return res.error_response('Expected day parameter in request body')

    Restaurant.objects.all().delete()
    Menu.objects.all().delete()

    try:
        restaurant_info_list = restaurant_upload_service.upload(request.data)
    except Exception as ex:
        return res.error_response(str(ex))

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
