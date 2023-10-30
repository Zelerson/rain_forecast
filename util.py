import requests
import re
import json
from os.path import exists
from datetime import datetime, timedelta


def rain_forecast(rain_sum):
    if rain_sum is None:
        print('Nie wiem')
    elif rain_sum > 0:
        print('Będzie padać')
    elif rain_sum == 0:
        print('Nie będzie padać')


class WeatherForecast:
    COORDS = {'Warsaw': (52.2298, 21.0118)}

    def __init__(self):
        self.data = {}
        if exists('rain_data.json'):
            with open('rain_data.json', 'r') as json_file:
                self.data = json.load(json_file)

    def __setitem__(self, key, value):
        self.data[key] = value

    def __getitem__(self, key):
        if key in self.data:
            return self.data[key]
        else:
            return self.get_rain_sum(key)

    def __iter__(self):
        return iter(self.data)

    def dump(self):
        with open('rain_data.json', 'w') as json_file:
            json.dump(self.data, json_file)

    def items(self):
        for key, value in self.data.items():
            yield key, value

    def fetch_rain_sum(self, searched_date: str, coords=COORDS['Warsaw']):
        url = (
            f'https://api.open-meteo.com/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=rain&daily=rain_sum'
            f'&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}')
        response = requests.get(url)

        if response.ok:
            data = response.json()
            self.data[searched_date] = data['daily']['rain_sum'][0]
            self.dump()

    def get_rain_sum(self, searched_date: str):
        if searched_date not in self.data:
            self.fetch_rain_sum(searched_date)

        return self.data.get(searched_date)


def date_input():
    date_pattern = r'^\d{4}-\d{2}-\d{2}$'
    date = input('Podaj datę w formacie YYYY-mm-dd: ')
    if re.match(date_pattern, date):
        return date
    elif date == '':
        tomorrow = datetime.now() + timedelta(days=1)
        return tomorrow.strftime('%Y-%m-%d')
    else:
        return None
