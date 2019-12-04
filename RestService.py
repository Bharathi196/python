# -*- coding: utf-8 -*-
"""
Created on Wed Nov 20 19:06:11 2019

@author: Bharathi
"""

from flask import Flask;
from flask_cors import CORS;

app = Flask(__name__)
CORS(app)

@app.route("/", methods=['GET'])

def index():
    return "Welcome to CodezUp"

if __name__ == '__main__':
    app.run(debug=True)