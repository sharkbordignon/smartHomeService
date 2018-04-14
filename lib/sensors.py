import sys
sys.path.append('config')
import setup_sensors as cfg

def listSensors(status):
  status = status.replace("'", "")
  list_sensors = cfg.setup["sensorsList"]
  if(status != None):
    return filter(lambda x: x['status'] == status, list_sensors)
  return list_sensors

#print listSensors('on')