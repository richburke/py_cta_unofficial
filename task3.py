import urllib.request
from xml.etree.ElementTree import parse
import time

ROUTE = '22'
TARGET_LAT = 41.98062
TARGET_LONG = -87.668452
history = dict()

def lat_distance_in_miles(v1, v2):
	# Multiplying by 69 returns value in miles
	return 69 * abs(v1-v2)

def monitor():
	u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=' + ROUTE)
	doc = parse(u)

	for bus in doc.findall('bus'):
		bus_id = bus.findtext('id')
		lat = float(bus.findtext('lat'))
		distance = round(lat_distance_in_miles(TARGET_LAT, lat), 2)

		trend = 'NEW'

		if bus_id not in history:
			history[bus_id] = lat
		else:
			past_delta = round(lat_distance_in_miles(TARGET_LAT, history[bus_id]), 2)

			trend = ''
			if distance > past_delta:
				trend = 'away'
			elif distance < past_delta:
				trend = 'toward'
			else:  # Bus is not moving
				trend = 'stopped or out of service'

		print(bus_id+' '+str(distance)+' miles [' + trend + ']')

	print('-'*10)

while True:
	monitor()
	time.sleep(30)
