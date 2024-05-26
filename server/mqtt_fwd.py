import paho.mqtt.subscribe as subscribe
from influxdb import InfluxClient

influxdb = InfluxClient()

while True:
	msg = subscribe.simple("diyPressoOne/#", hostname="test.mosquitto.org", port=1883)
	print("%s %s" % (msg.topic, msg.payload))
	influxdb.write_line(msg.payload.decode())
	influxdb.send()