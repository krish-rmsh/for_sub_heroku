# -*- coding: utf-8 -*-
"""
Created on Mon Feb 21 20:18:06 2022

@author: Krish_Ramesh
"""
import numpy as np
import pandas as pd
import pickle

#from __main__ import *
    # load the pre-trained Keras model

    #tfidf = pickle.load('tf_idf.sav')
with open("data/sentiment_analysis.sav","rb") as f:
     model = pickle.load(f)  
with open("data/recommender.sav","rb") as f:
     recommender = pickle.load(f)
     
#user_input = str(input("Enter your user name"))
#user_input = 'mike'
def recom_printer(user_input):
    print('username input: ',user_input)

    if user_input in recommender.index.tolist(): 
        top20 = recommender.loc[user_input].sort_values(ascending=False)[0:20]
#print(top20)
        recomended_prods = top20.index
        data = pd.read_csv(r"data/sample30_cleaned.csv") # This should be cleaned data
        data = data[data.id.isin(recomended_prods)] # refining only those products
        refine_recom = data.pivot_table(values = 'user_senti_encode', index = 'id+name', aggfunc='mean').sort_values(by= 'user_senti_encode', ascending=False)
        #print(refine_recom[:5])
        #return render_template('simple.html',  tables=[df.to_html(classes='data', header="true")])
        refine_recom.drop(columns = ['user_senti_encode'],inplace = True)
        refine_recom['id+name'] = refine_recom.index
       # print(refine_recom)
        refine_recom[['id', 'product_name']] = refine_recom['id+name'].str.split(';', expand=True)
        #print(refine_recom.columns)
        refine_recom.drop(columns = ['id+name'],inplace = True)
        #print(refine_recom)
        #refine_recom.rename(columns={'0': 'id', '1': 'name of product'}, inplace=True)
        return refine_recom[:5].to_html(index=False)
    else:
        return "The name is not there"
