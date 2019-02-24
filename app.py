from flask import Flask,render_template,request,session,redirect
import pandas as pd
import numpy as np
import os
import random

import mysql.connector


import re 
import requests
import codecs
import pandas as pd
import html
requests.packages.urllib3
app= Flask(__name__)



@app.route('/')
def land():
    return render_template('land.html')
@app.route('/customer.html')
def test():
    return render_template('customer.html')
@app.route('/customer1.html', methods = ['POST'])
def test1():
    males=request.form['males']
    females=request.form['females']
    mini=request.form['min']
    maxi=request.form['max']
    park=request.form['park']
    bd=request.form['bd']
    area=request.form['area']
    path=os.getcwd()+"\\filtered3.csv"
    raw_data=pd.read_csv(path)
    print(path)
    l=[]
    low=(int)(mini)
    high=(int)(maxi)
    bhk=(int)(bd)
    parking=(int)(park)
    data=raw_data.loc[raw_data['AREA'] == area]
    e_data=data[(data["Estimate"]>=low) & (data["Estimate"]<=high)]

    
    r_data=e_data[(e_data["N_ROOM"]==bhk)]

    print(r_data)
    r_data.to_csv('result.csv')
    return render_template('list.html', n = area)






app.run(debug=True)
