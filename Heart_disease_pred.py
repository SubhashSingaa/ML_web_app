# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 17:26:41 2025

@author: s.v.subhash reddy
"""

#Import Dependencies
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#Loading the saved Model
heart_model=pickle.load(open("heart_disease_model.sav","rb"))

#Siderbar/Navigationbar to Navigate
with st.sidebar:
    selected=option_menu("Heart Disease Prediction", ["Heart Disease"],default_index=0)
    
#Heart disease prediction page
if(selected == "Heart Disease"):
    st.title("Heart Disease Prediction")
    
    col1,col2,col3=st.columns(3)
    with col1:
        age=st.number_input("Enter the age")
    with col2:
        sex=st.number_input("Enter the gender")
    with col3:
        cp=st.number_input("Enter the Chest pain")
    with col1:
        trestbps=st.number_input("Enter the trestbps")
    with col2:
        chol=st.number_input("Enter the chol")
    with col3:
        fbs=st.number_input("Enter the fbs")
    with col1:
        restecg=st.number_input("Enter the restecg")
    with col2:
        thalach=st.number_input("Enter the thalach")    
    with col3:
        exang=st.number_input("Enter the exang")
    with col1:
        oldpeak=st.number_input("Enter the oldpeak")
    with col2:
        slope=st.number_input("Enter the slope")
    with col3:
        ca=st.number_input("Enter the ca")
    with col1:
        thal=st.number_input("Enter the thal")
    
    #code for prediction
    heart_pred=''
    
    #creating a button
    if st.button("Heart Disease Result"):
        heart=heart_model.predict([[age,sex,cp,trestbps,chol,fbs, restecg,thalach,exang,oldpeak,slope,ca,thal]])
        
        if(heart[0]==1):
            heart_pred="The person has Heart Disease"
        else:
            heart_pred="The person does not have Heart Disease"
    st.success(heart_pred)
