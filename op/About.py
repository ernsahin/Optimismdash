import streamlit as st
import altair as alt
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
from shroomdk import ShroomDK

st.set_page_config(layout="wide")
coz1, coz2, coz3 = st.columns(3)
 
with coz1:
    st.write(' ')

with coz2:
    st.image("logo2.png")

with coz3:
    st.write(' ')
# header = st.container()
dataset= st.container()
# features= st.container()
modelTraining= st.container()
 
st.markdown("<h1 style='text-align: center; color: White;'> Optimism Megadashboard </h1>", unsafe_allow_html=True)
 

# Sidebar setup

#Sidebar navigation
st.sidebar.title('Data Frame')
options = st.sidebar.radio('Select what you want to display:', ['About','Findings'])
 
fig=go.Figure()
api1= pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/20bce94b-11bc-46bd-83bf-896b004af3a8/data/latest",orient='columns') 
api2=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest",orient='columns')
api3=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/a24671ce-7a08-4db6-a303-a309841b9dce/data/latest",orient='columns')
# st.write(api1.head())
# st.write(api1)

def stats():
    st.header("Welcome To The Optimism Megadashboard")
    st.markdown("#### In this megadashboard we will be looking at the Optimism, metrics we will be looking at is Transactions, Blocks, Contracts and Staking. This dashboard is made with using Flipside API, bounty question comes from MetricsDAO")
    st.markdown('##### Charts are updated at every 12 hours.')
    st.write("###  [Flipside Crypto](https://flipsidecrypto.xyz)")  
    st.write("###  [Metrics DAO](https://metricsdao.xyz)")  
    st.write("###  [Github](https://github.com/ernsahin/Optimismdash)")  
def findings():
    st.header("Some Findings About Optimism")
    st.markdown("#### Optimism Chain is currently living its best times by far, in all metrics they are showing improvments, while more contracts are deployed number of users is increasing as well , self delegation has surpased the first time delegators people started to delegate themselves more than the others , number of transactions has increased nearly 4x since July 4M transaction in a week is now a normal thing for Optimism chain, gas use and tps has increased as well. So 2023 could be the year of Optimism chain with all metrics increasing in this market conditions.")

if options=='About':
    stats()
elif options=='Findings':
    findings()


 