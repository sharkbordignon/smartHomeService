#!/usr/bin/env python
import sys
sys.path.append('../config')
import setup_sensors as sensors


def listSensors(status):
  list_sensors = sensors.setup["sensorsList"]
  if(status != None):
    return filter(lambda x: x['status'] == status, list_sensors)
  return list_sensors