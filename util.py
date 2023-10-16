import requests
import re
import json
from os.path import exists
from datetime import datetime, timedelta


def fetch_rain_sum(searched_date: str, coords: tuple):
    url = (
        f'https://api.open-meteo.com/v1/forecast?latitude={coords[0]}&longitude={coords[1]}&hourly=rain&daily=rain_sum'
        f'&timezone=Europe%2FLondon&start_date={searched_date}&end_date={searched_date}')
    response = requests.get(url)

    if response.ok:
        data = response.json()
        return data['daily']['rain_sum'][0]
    else:
        return None


def get_rain_sum(searched_date: str, rain_data, coords: tuple):
    if searched_date not in rain_data:
        rain_sum = fetch_rain_sum(searched_date, coords)

        if rain_sum is not None:
            rain_data.append({searched_date: rain_sum})
            with open('rain_data.json', 'w') as json_file:
                json.dump(rain_data, json_file)

        return rain_sum
    else:
        return rain_data[searched_date]


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


def load_rain_data():
    if exists('rain_data.json'):
        with open('rain_data.json', 'r') as json_file:
            return json.load(json_file)
    else:
        return []
