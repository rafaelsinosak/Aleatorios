from pprint import pprint
import json, requests
r = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Sao Jose dos Campos&APPID=[SuaID]')

pprint(r.json())

data = json.loads(r.content)

print "Cidade:",data['name'],"\nTemperatura Maxima:",data['main']['temp_max'],"\nTemperatura Minima:",data['main']['temp_min']



