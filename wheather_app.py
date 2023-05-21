import requests

openweather_KEY = ''
city = 'none'
openweather_link = f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={openweather_KEY}'


try:
    while city != 'EXIT':
        print('--Weather App--')
        city = str(input('Type the city name, (Type EXIT for ending): '))
        if city != 'EXIT':
            print(f'Weather in: {city}')
            req = requests.get(openweather_link)
            req_data = req.json()
            weather = req_data['weather'][0]['description']
            temp = req_data['main']['temp']
            print('clima: ', weather, 'temperatura', temp)

except (TypeError, ValueError):
    print('ERROR! invalid entry')


print('Ending Weather App')
