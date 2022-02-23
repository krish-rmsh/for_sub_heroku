# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 17:34:04 2022

@author: Krish_Ramesh
"""

import pickle
import pandas as pd
import re
from flask import Flask, request, render_template
import model
from __main__ import *


app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('summa.html')

@app.route('/', methods=['POST'])
def my_form_post():
    text = request.form['text']

    #strip_special_chars = re.compile("[^A-Za-z0-9 ]+")
    text = text.lower().replace("<br />", " ")
    text = re.sub(' +', ' ',text.strip())
    #text=re.sub(strip_special_chars, "", text.lower())

    refine_recom = model.recom_printer(text)
    
    return refine_recom

@app.route('/reco')
def reco_home():
    return render_template('summa.html')
if __name__ == "__main__":
    app.run()