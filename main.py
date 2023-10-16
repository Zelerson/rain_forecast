import util


COORDS = {'Warsaw': (52.2298, 21.0118)}


rain_data = util.load_rain_data()
searched_date = util.date_input()

rain_sum = util.get_rain_sum(searched_date, rain_data, COORDS['Warsaw'])

if rain_sum is None:
    print('Nie wiem')
elif rain_sum > 0:
    print('Będzie padać')
elif rain_sum == 0:
    print('Nie będzie padać')

