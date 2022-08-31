import json
from os import listdir


def upload(request_data):
    onlyfiles = [f for f in listdir('/lunchplace/api/static/restaurants')]
    list_names = [names.rstrip('.json') for names in onlyfiles]
    data = []
    for restaurant_name in list_names:
        file = open("/home/denis/PycharmProjects/LunchPlace/lunchplace/api/static/restaurants/" + restaurant_name + '.json')
        restaurant_info = json.load(file)
        data.append({'name': restaurant_name,
                     'description': restaurant_info['description'],
                     'phone_number': restaurant_info['phone_number'],
                     'menu': restaurant_info['menu'][request_data['day']]})

    return data
