#!/usr/bin/env python
import os
import json

BASE_DIRECTORY = "/sys/bus/w1/devices"
SLAVE_FILE = "w1_slave"

def listSensors():
    sensors = []
    for i in os.listdir('/sys/bus/w1/devices'):
        if i != 'w1_bus_master1':
            sensors.append(i)
    return json.dumps(sensors)

def read(sensor):
    location = '/sys/bus/w1/devices/' + str(sensor) + '/w1_slave'
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit

def read2(sensor):
    location =  os.path.join(BASE_DIRECTORY,sensor, SLAVE_FILE)
    tfile = open(location)
    text = tfile.read()
    tfile.close()
    secondline = text.split("\n")[1]
    temperaturedata = secondline.split(" ")[9]
    temperature = float(temperaturedata[2:])
    celsius = temperature / 1000
    farenheit = (celsius * 1.8) + 32
    return celsius, farenheit
