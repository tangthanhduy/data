import Adafruit_DHT
import time
from time import sleep
from gpiozero import InputDevice 
from BMP180 import BMP180
import requests

#Set pin for DHT sensor
DHTpin = 22
#Set pin for Rain sensor
no_rain = InputDevice(18)


while True:
    bmp = BMP180()
    sensor = Adafruit_DHT.DHT11
    DHThumidity, DHTtemperature = Adafruit_DHT.read_retry(sensor, DHTpin)
    BMPpressure = bmp.read_pressure()
    BMPtemperature = bmp.read_temperature()
    BMPaltitude = bmp.read_altitude()
    if not no_rain.is_active:
        rain = 1
    else:
        rain = 0
    #put the results in dictionary
    data = {"device_name": "Weather-IoT-Device", "BMPtemperature": BMPtemperature, "BMPpressure": BMPpressure, "BMPaltitude": BMPaltitude, "DHTtemperature": DHTtemperature, "DHThumidity": DHThumidity, "Raining":rain}
    #API for post the request
    url = "http://20.36.36.132:8000/api/create_post"
    try:
        #Post the requet
        response = requests.post(url,data)
        print(response)
    except Exception as e:
        print(e)
        print(response)
    #Set time for executing the while loop
    sleep(300)
    
