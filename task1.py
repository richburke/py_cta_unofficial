
import urllib.request
import urllib.error
#import requests

ROUTE = '22'
# u = urllib2.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=' + ROUTE)
#data = requests.get('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=' + ROUTE)
u = urllib.request.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=' + ROUTE)
data = u.read()

f = open('rt'+ROUTE+'.xml', 'wb')
f.write(data)
f.close()
