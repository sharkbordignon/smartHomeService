from flask import Flask
import os
import lib.ds18b20 as ds18b20

app = Flask(__name__)

# Routes here #

@app.route('/api/ds18b20/getAll')
def getAll():
  return ds18b20.listSensors()

@app.route('/api/ds18b20/getTempetature/<sensor>')
def getTempetature(sensor):
  return ds18b20.read(sensor)

@app.route('/api/ds18b20/getTempetature2/<sensor>')
def getTempetature2(sensor):
  return ds18b20.read2(sensor)

# Main #

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=2121)