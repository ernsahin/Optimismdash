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
# api='53012785-d2f9-49a0-81a9-cdd22bc8a330'
# sdk = ShroomDK(api)
st.markdown("<h1 style='text-align: center; color: White;'> Optimism Megadashboard </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: Red;'> Block Performance Of Optimism </h2>", unsafe_allow_html=True)

# Sidebar setup

#Sidebar navigation
st.sidebar.image('pages/logo.png')
st.sidebar.title('Data Frame')
options = st.sidebar.radio('Select what you want to display:', ['Daily Data', 'Weekly Data'])
# date=''
# date=st.slider(
#         "How Many Days You Want For Your Data",
#         min_value=0,
#         value=360
#         ) 

 
api1= pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/20bce94b-11bc-46bd-83bf-896b004af3a8/data/latest",orient='columns') 
api2=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest",orient='columns')
api3=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/a24671ce-7a08-4db6-a303-a309841b9dce/data/latest",orient='columns')
api4=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/908b6aa0-dff7-487c-9083-15fcd54a2d52/data/latest",orient='columns')
api5=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d/data/latest",orient='columns')
api6=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d/data/latest",orient='columns')
 


ab1,ab2,ab3 = st.columns(3)
ab4,ab5,ab6= st.columns(3)
ab1.metric("Average Time Between Blocks",api1["AVG_TIME_BLOCKS"])
ab2.metric("Max Time Between Blocks",api1["MAX_TIME_BLOCKS"])
ab3.metric("Min Time Between Blocks",api1["MIN_TIME_BLOCKS"])
ab4.metric("Average Transaction Per Block",api1["AVG_TX_PER_BLOCK"])
ab5.metric("Min Transaction Per Block",api1["MIN_TX_PER_BLOCK"])
ab6.metric("Average Difficulty",api1["AVG_DIFFICULTY"])

 
def data(dataframe) :
    blocks,blocks2=st.columns(2)
    with blocks : 
        st.title('Avg Time Between Blocks') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='AVG_TIME_BLOCKS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/908b6aa0-dff7-487c-9083-15fcd54a2d52\">Query Link</a><br>",
            
        )
        chart_daily.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    )
)
        st.plotly_chart(chart_daily,use_container_width=True)
         
    with blocks2:   
       
        st.title('Max Time Between Blocks') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='MAX_TIME_BLOCKS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/908b6aa0-dff7-487c-9083-15fcd54a2d52\">Query Link</a><br>",
        )   
        chart_daily.update_xaxes(
        rangeslider_visible=True,
        
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    )
)
        st.plotly_chart(chart_daily,use_container_width=True)
def data2(dataframe) :
    blocks,blocks2=st.columns(2)
    with blocks : 
        st.title('Avg Time Between Blocks') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='AVG_TIME_BLOCKS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d\">Query Link</a><br>",
            
        )
        chart_daily.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    )
)
        st.plotly_chart(chart_daily,use_container_width=True)
         
    with blocks2:   
       
        st.title('Max Time Between Blocks') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='MAX_TIME_BLOCKS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d\">Query Link</a><br>",
            
            
        )   
        chart_daily.update_xaxes(
        rangeslider_visible=True,
        
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
    )
)
        st.plotly_chart(chart_daily,use_container_width=True)

     

   


 
if options=='Daily Data':
    data(api4)
elif options=='Weekly Data':
    data2(api5)

 