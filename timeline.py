from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, RadioField, validators
import requests
import json
import os
import codecs
import pandas as pd
from datetime import datetime
from elasticsearch import Elasticsearch
# from pymongo import MongoClient # Database connector
#from bson.objectid import ObjectId # For ObjectId to work

#APP settings
app = Flask(__name__)  


#CONNECT TO MONGODB
#client = MongoClient('localhost', 27017)    #Configure the connection to the database
""" db = client.timeline                    #Select the database
tline = db.study                            #Select the collection """
#db = client.timeline                        #Select the database
#tline = db.stl_data                            #Select the collection

tline="some text"
title = "Timeline Example"
heading = "List Details"
#modify=ObjectId()

@app.route("/home")
def home():
    return render_template('index2.html',t=title,h=heading)

@app.route("/tline")
def timel ():
    a1="active"
    return render_template('index.html',a1=a1,t=title,h=heading)

@app.route("/tline_st")
def timel_st ():
    a1="active"
    return render_template('index_scatter.html',a1=a1,t=title,h=heading)

@app.route("/tline_st1")
def timel_st1 ():
    a1="active"
    return render_template('timeline_st1.html',tline=tline,a1=a1,t=title,h=heading)

@app.route("/tlined3")
def timeld3 ():
    a1="active"
    return render_template('timelined3.html',tline=tline,a1=a1,t=title,h=heading)

@app.route("/test")
def test ():
    a1="active"
    return render_template('test.html',tline=tline,a1=a1,t=title,h=heading)

@app.route("/about") 
def about():
    return render_template('credits.html',t=title,h=heading)


if __name__ == "__main__":
    app.secret_key='secret456'
    app.run('0.0.0.0',8015,debug=True)
    #app.run(port=5005,debug=True)
