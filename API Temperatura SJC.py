from pprint import pprint
import json, requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Sao Jose dos Campos&APPID=c45d6487bfa01764e2f05d0ff1cac8d6')

pprint(r.json())

data = json.loads(r.content)

print "Cidade:",data['name'],"\nTemperatura Maxima:",data['main']['temp_max'],"\nTemperatura Minima:",data['main']['temp_min']



