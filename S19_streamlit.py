import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello Welcome")
df = pd.DataFrame(np.random.randn(20,3),columns=['a','b','c'])
st.write("Here is random data")
st.write(df)
st.write("Here is line chart")
st.line_chart(df)

#Widgets
st.title("Widgets")
name=st.text_input("What is your Name")
st.write(f"Hi {name}")
age=st.slider("Enter your age",0,100,18)
st.write(f"Your age is {age}")
options=['a','b','c']
choice=st.selectbox("Select one option",options)
upload_file=st.file_uploader("Choose file")