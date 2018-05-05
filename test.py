import requests
# import urllib3, urllib, json
import grab

api_key = 'b68e96fab0e75cebaa93fcfe0a5fce58'
api_call = f'http://api.openweathermap.org/data/2.5/forecast?id=524901&APPID={api_key}'
city_id = '520068'
get_cels = requests.get(f'http://api.openweathermap.org/data/2.5/weather?id={city_id}&units=metric&appid={api_key}')

# respond = get_cels.json()
# print(respond)
#
# # a = {'coord': {'lon': 38.44, 'lat': 55.87}, 'weather': [{'id': 520, 'main': 'Rain', 'description': 'light intensity shower rain', 'icon': '09d'}], 'base': 'stations', 'main': {'temp': 7, 'pressure': 1008, 'humidity': 87, 'temp_min': 7, 'temp_max': 7}, 'visibility': 10000, 'wind': {'speed': 6, 'deg': 300}, 'clouds': {'all': 75}, 'dt': 1524061800, 'sys': {'type': 1, 'id': 7322, 'message': 0.0029, 'country': 'RU', 'sunrise': 1524017558, 'sunset': 1524069579}, 'id': 520068, 'name': 'Noginsk', 'cod': 200}
# #
# city = respond.get('name')
# temp = respond.get('main').get('temp')
#
# print(f'В {city} {temp} градусов')

