# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 11:44:37 2022

@author: deepak
"""
import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
st.set_option('deprecation.showfileUploaderEncoding', False)
# Load the pickled model
model = pickle.load(open('Randomforestmodel.pkl', 'rb'))  
def predict_note_authentication(UserID, Gender,Age,EstimatedSalary):
  output= model.predict([[Gender, Age,EstimatedSalary]])
  print("Purchased", output)
  if output==[1]:
    prediction="Item will be purchased"
  else:
    prediction="Item will not be purchased"
  print(prediction)
  return prediction
def main():
    
    html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Department of Computer Engineering</p></center> 
   <center><p style="font-size:25px;color:white;margin-top:10px;"Machine Learning Lab Experiment</p></center> 
   </div>
   </div>
   </div>
   """
    st.markdown(html_temp,unsafe_allow_html=True)
    st.header("Item Purchase Prediction using K nearest neighbor Algorithm")
    
    UserID = st.text_input("UserID","Type Here")
    
    Gender1 = st.select_slider('Select a Gender Male:1 Female:0',options=['1', '0'])
    Age = st.number_input('Insert a Age',18,60)
   
    EstimatedSalary = st.number_input("Insert Estimated Salary",15000,150000)
    resul=""
    if st.button("Predict"):
      result=predict_note_authentication(UserID, Gender1,Age,EstimatedSalary)
      st.success('Model has predicted {}'.format(result))
      
    if st.button("About"):
      st.subheader("Developed by Deepak Moud")
      st.subheader("Head , Department of Computer Engineering")

if __name__=='__main__':
  main()