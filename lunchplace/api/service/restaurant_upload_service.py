import json
import pathlib
from os import listdir


def upload(request_data):
    """Uploading data from Restaurant files"""
    only_files = [f for f in listdir(str(pathlib.Path().absolute()) + '/api/static/restaurants')]
    list_names = [names.rstrip('.json') for names in only_files]
    data = []
    requested_day = request_data['day']

    for restaurant_name in list_names:
        file = open(str(pathlib.Path().absolute()) + '/api/static/restaurants/' + restaurant_name + '.json')
        restaurant_info = json.load(file)

        restaurant_info_menu = restaurant_info['menu']

        if requested_day not in restaurant_info_menu:
            raise Exception(f'{requested_day} not in menu for {restaurant_name}')

        data.append({'name': restaurant_name,
                     'description': restaurant_info['description'],
                     'phone_number': restaurant_info['phone_number'],
                     'menu': restaurant_info_menu[requested_day]})

    return data
