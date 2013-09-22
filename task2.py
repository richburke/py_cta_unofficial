
from xml.etree.ElementTree import parse
import webbrowser

ROUTE = '22'
TARGET_LAT = 41.98062
TARGET_LONG = -87.668452

def lat_distance_in_miles(v1, v2):
	# Multiplying by 69 returns value in miles
	return 69 * abs(v1-v2)


doc = parse('rt'+ROUTE+'.xml')

for bus in doc.findall('bus'):
	lat = float(bus.findtext('lat'))

	if lat >= TARGET_LAT:
		bus_id = bus.findtext('id')
		direction = bus.findtext('d')

		if lat == TARGET_LAT:
			print(bus_id + ' It\'s here!')
		if lat > TARGET_LAT and direction.startswith('South'):
			distance = lat_distance_in_miles(TARGET_LAT, lat)
			print(bus_id + ' It\'s headed our way. ('+str(lat)+', +'+str(lat-TARGET_LAT) + ', '+str(round(distance, 2))+' miles, '+direction+')')

			lon = bus.findtext('lon')
			url = 'http://maps.googleapis.com/maps/api/staticmap?center=Chicago,IL&zoom=11&size=1200x800&sensor=false&maptype=roadmap'
			url = url + '&markers=color:green%7Clabel:bus%7C'+str(lat)+','+lon
			webbrowser.open(url)

