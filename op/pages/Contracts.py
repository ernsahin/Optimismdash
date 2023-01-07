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
    st.image("https://github.com/ernsahin/Optimismdash/blob/main/logo2.png?raw=true")

with coz3:
    st.write(' ')
# header = st.container()
dataset= st.container()
# features= st.container()
modelTraining= st.container()
 
st.markdown("<h1 style='text-align: center; color: White;'> Optimism Megadashboard </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: Red;'> Transaction Performance Of Optimism </h2>", unsafe_allow_html=True)
st.sidebar.image('https://github.com/ernsahin/Optimismdash/blob/main/logo.png?raw=true')
st.sidebar.title('Data Frame')
options = st.sidebar.radio('Select what you want to display:', ['Daily Data', 'Weekly Data'])
 
fig=go.Figure()
api1= pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/20bce94b-11bc-46bd-83bf-896b004af3a8/data/latest",orient='columns') 
api7=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/bed7c24b-2054-4803-a871-770f26bb47a0/data/latest",orient='columns')
api3=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/a24671ce-7a08-4db6-a303-a309841b9dce/data/latest",orient='columns')
topcontracts=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/224212f8-eb0f-4f29-9dee-0a34de69405d/data/latest",orient='columns')
api5=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d/data/latest",orient='columns')
api6=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb/data/latest",orient='columns')

# st.write(api1.head())
# st.write(api1)

def stats():
    st.header("Welcome To The Optimism Megadashboard")
    st.text("In this megadashboard we will be looking at the ")
def data(dataframe) :
    transactions,transactions2=st.columns(2)
    with transactions : 
        st.title('Contracts Deployed Daily') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='NEW_CONTRACTS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/bed7c24b-2054-4803-a871-770f26bb47a0\">Query Link</a><br>",
            
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
         
    with transactions2:   
       
        st.title('Contracts Deployed Cumulative') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='CUMULATIVE_CONTRACTS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/bed7c24b-2054-4803-a871-770f26bb47a0\">Query Link</a><br>",
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
        st.title('Transactions') 
        chart_daily = px.bar(
            dataframe,
            x='DATE_WEEK',
            y='NEW_CONTRACTS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/bed7c24b-2054-4803-a871-770f26bb47a0\">Query Link</a><br>",
            
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
       
        st.title('Status Of Transactions') 
        chart_daily = px.area(
            dataframe,
            x='DATE_WEEK',
            y='CUMULATIVE_CONTRACTS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/bed7c24b-2054-4803-a871-770f26bb47a0\">Query Link</a><br>",            
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
tops=st.container()
api10=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/5baab71c-2c7c-43a1-8e0a-e22edaf3173d/data/latest',orient='columns')
api11=pd.read_json('https://node-api.flipsidecrypto.com/api/v2/queries/8ced3001-7a84-4331-9558-14e270086bd4/data/latest',orient='columns')
with tops : 
        st.title('Top 20 Contracts OF Optimism By Use TXs') 
        chart_daily = px.bar(
            topcontracts,
            x='CONTRACT',
            y='USE',
            color='CONTRACT',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/224212f8-eb0f-4f29-9dee-0a34de69405d\">Query Link</a><br>",
            
        )
        st.plotly_chart(chart_daily,use_container_width=True)
        st.title('Top 20 Contracts By Users') 
        chart_daily = px.bar(
            api10,
            x='CONTRACT',
            y='USERS',
            color='CONTRACT',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/5baab71c-2c7c-43a1-8e0a-e22edaf3173d\">Query Link</a><br>",
            
        )
        st.plotly_chart(chart_daily,use_container_width=True,theme='streamlit')
        st.title("Weekly Top 10 Contracts By USE")
        chart_daily = px.bar(
            api11,
            x='DATE',
            y='USE',
            color='CONTRACT',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/8ced3001-7a84-4331-9558-14e270086bd4\">Query Link</a><br>",
            
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
         
        st.plotly_chart(chart_daily,use_container_width=True,theme='streamlit')


        

     

   


if options=='Home':
    stats()
elif options=='Daily Data':
    data(api7)
elif options=='Weekly Data':
    data2(api7)
expander=st.expander("See The Analysis")
expander.write("  \
             Date For The Analysis '2023-07-01' \
             .Number of contracts deployed is increasing since the November, 2k contracts in a day is becoming a normal things for Optimism \ Most used contracts are mostly comes from bridge protocols like Hop \ Use of USDC bridge has increased recently with new protocols like Pika.   ")
