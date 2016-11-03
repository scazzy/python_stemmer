#!/usr/local/bin/python
from flask import Flask
import stem
app = Flask(__name__)

@app.route('/')
def index():
  return "API for some data programs"

@app.route('/stem', methods=['GET', 'POST'])
def stemRoute():
  return stem.job()

if __name__ == '__main__':
  app.run(debug=True,host='0.0.0.0',port=5000)
