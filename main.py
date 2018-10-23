# -*- coding: utf-8 -*-
"""
Created on Mon Oct 22 09:57:19 2018

@author: Mahsa
"""

from flask import Flask, flash, redirect, render_template, request, session, abort
import foodTruck
import requests

app = Flask(__name__)

@app.route('/') 
@app.route("/home")
def index():
     user=foodTruck.latlong()
     return render_template('index.html', user=user)
     
@app.route('/home/response/truck', methods=['GET'])
def food():
    return foodTruck.index();


if __name__ == "__main__":
    app.run(host='0.0.0.0')