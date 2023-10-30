from util import WeatherForecast, date_input, rain_forecast


weather_forecast = WeatherForecast()


print('1. Deszcz dla konkretnej daty')
print('2. Wszystkie zapisane daty')
print('3. Wszystkie zapisane pary data: opady deszczu w mm')
command = input('Wprowadź numer komendy: ')

match command:
    case '1':
        searched_date = date_input()
        rain_sum = weather_forecast[searched_date]
        rain_forecast(rain_sum)
    case '2':
        for x in weather_forecast:
            print(x)
    case '3':
        for date, rain in weather_forecast.items():
            print(f'{date}: {rain}')