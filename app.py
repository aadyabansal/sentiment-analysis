import streamlit as st
import sklearn
import joblib
model = joblib.load('Sentiment_Analysis (1)')
st.title('Sentiment Analysis')
ip = st.text_input("Enter the message")
op = model.predict([ip])
if st.button('Predict'):
  st.title(op[0])
   
