import pandas as pd 
import streamlit as st
import plotly.express as px 
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np



st.set_page_config(page_title="Data Analysis :bar_chart",
page_icon=':bar_chart:', layout="centered",
initial_sidebar_state="auto")
st.header('Data Analysis :bar_chart:')
st.subheader('The Covid Worldwide Statistic')
 
 # title of the app 
csv_file = 'covid_worldwide.csv'
sheet_name = 'DATA'
 


#image of the app
Image = Image.open('images/Covid.jpeg')
st.image(Image,
         width=500)





df_csv=pd.read_csv('covid_worldwide.csv')
df_csv
                
st.sidebar.header('You can choose the country here:')
Country = st.sidebar._multiselect(
        'select a country:',
        options=df_csv['Country'].unique(),
        default=df_csv['Country'].unique()

)

country_data = pd.DataFrame({
    'country': ['USA', 'India', 'France' , 'Germany' ,'Brazil', 'Japan','S. Korea','Italy','UK','Russia'],
    'cases': [ 104196861 , 44682784, 39524311 , 37779833,36824580, 32588442, 30197066 ,25453789 , 24274361, 21958696],
    'total deaths':[ 104196861 , 44682784, 39524311 , 37779833,36824580, 32588442, 30197066 ,25453789 , 24274361, 21958696]
})

# Statistics On A  Map
st.write("## Top 50  country on the world")
df = pd.DataFrame(
    np.random.randn(100, 2) / [50, 50] + [37.76, -122.4],
    columns=['lat', 'lon'])
st.map(df)
                
                


# the bar chart 

st.write("## Top 10  country")

st.bar_chart(country_data)

Data1 = [60,36,80]
labels=['Active Cases','Total test','Population']
explode=[0,0,0.2]


fig, ax = plt.subplots()
st.write("## Top 10  country around the world")
ax.pie(Data1, labels=labels, colors=['green', 'yellow', 'red'], autopct='%.0f%%', shadow=True, explode=explode)
ax.set_title('')

st.pyplot(fig)

