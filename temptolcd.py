#!/usr/bin/python
from lcd2 import *
import Adafruit_DHT

sensor = Adafruit_DHT.DHT11
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
hum = str(humidity)
fah = 9.0/5.0 * temperature + 32

if humidity is not None and temperature is not None:
#	print 'Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity)
	t = 'Temp: %sF' % fah
#	print hum
#	print type(humidity)
	h = 'Humidity: {0:0.2f}%'.format(humidity)
	derp = " %s \n%s" % (t,h)
	lcd = lcd = HD44780()
	lcd.message(derp)
else:
	print 'Failed to get reading. Try again!'

