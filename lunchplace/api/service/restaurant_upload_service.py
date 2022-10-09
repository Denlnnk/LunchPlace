from ..connections.s3_connection import S3Connection


def upload(request_data):
    """Uploading data from Restaurant files"""
    s3_connection = S3Connection()
    restaurants_info = s3_connection.load_files_content()
    data = []
    requested_day = request_data['day']

    for restaurant_info in restaurants_info:
        restaurant_info_menu = restaurant_info['menu']

        if requested_day not in restaurant_info_menu:
            raise Exception(f'{requested_day} not in menu for {restaurant_info["restaurant_name"]}')

        data.append({'restaurant_name': restaurant_info['restaurant_name'],
                     'description': restaurant_info['description'],
                     'phone_number': restaurant_info['phone_number'],
                     'menu': restaurant_info_menu[requested_day]})
    return data
