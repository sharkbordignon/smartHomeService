#!/usr/bin/env python
import sys
sys.path.append('utils')
import spreadsheet as ss
import utils.screen as screen

import lib.sensors as sensors
import datetime
import json
import time

if __name__ == '__main__':
  try:
    while True:
      available_sensors = json.loads(sensors.listSensors('on'))
      temperature_sensores = filter(lambda x: x['type'] == 'temperature', available_sensors)
      if temperature_sensores != []:
        msg = []
        msg.append(str(datetime.datetime.now()))
        msg.append(str(===xxx===xxx===))
        import lib.ds18b20 as ds18b20
        for x in temperature_sensores:
          temperature = json.loads(ds18b20.read(x['name']))[0][1]
          msg.append(str(temperature) + ' Celsius')
          ss.insertRow(x['nickname'], str(datetime.datetime.now()), temperature)
        screen.showStats(text)
      time.sleep(60)
  except KeyboardInterrupt:
    print 'ERROOORRRRRR'