from flask import Flask

app = Flask(__name__)

# Routes here #

# Sample #
@app.route('/path')
def method():
  return'something'

# Main #

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=2121)