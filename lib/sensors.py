import sys
sys.path.append('config')
import setup_sensors as cfg

import json

def listSensors(status):
  list_sensors = cfg.setup["sensorsList"]
  if(status != None):
    return json.dumps(filter(lambda x: x['status'] == status, list_sensors))
  return json.dumps(list_sensors)

#print listSensors('on')