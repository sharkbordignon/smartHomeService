from flask import Flask
import os
import lib.sensors as sensors
import lib.ds18b20 as ds18b20
import utils.screen as screen


app = Flask(__name__)

# Routes here #
@app.route('/api/sensors/getAll/<status>')
def getAllSensors(status):
  return sensors.listSensors(status.replace("'", ""))

@app.route('/api/ds18b20/getAll')
def getAlltemperatures():
  return ds18b20.listSensors()

@app.route('/api/ds18b20/getTempetature/<sensor>')
def getTempetature(sensor):
  return ds18b20.read(sensor.replace("'", ""))


@app.route('/api/screen/<text>')
def checkScreen(text):
  screen.showStats(text)
  return 'ok'
# Main #

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=2121)