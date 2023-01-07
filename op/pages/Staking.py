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
    st.image("https://github.com/ernsahin/Optimismdash/blob/main/op/logo2.png?raw=true")

with coz3:
    st.write(' ')
dataset= st.container()
 
modelTraining= st.container()
st.markdown("<h1 style='text-align: center; color: White;'> Optimism Megadashboard </h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; color: Red;'> Staking Performance Of Optimism </h2>", unsafe_allow_html=True)
 
st.sidebar.image('https://github.com/ernsahin/Optimismdash/blob/main/op/pages/logo.png?raw=true')
st.sidebar.title('Data Frame')



options = st.sidebar.radio('Select what you want to display:', [ 'Weekly Data'])
 
fig=go.Figure()
api1= pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/99f380b5-8faa-4df8-bbd4-4a63e1f81045/data/latest",orient='columns') 
 
 

 
 
def data(dataframe) :
    transactions,transactions2=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Charts Show The Delegated Amount + Delegations with Delegation Type. \
             Date For The Analysis '2023-07-01' \
             . At the launch of the OP Token we can see that first time delegators was much higher than self delegators as expected but in December first time delegators started to delegate for themselves and their volume + delegations are higher than the normal first time delegators.  ")
    cont=st.container()
    with transactions : 
        st.title('Weekly Delegations') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='DELEGATIONS',
            color='DELEGATION_TYPE',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/99f380b5-8faa-4df8-bbd4-4a63e1f81045\">Query Link</a><br>",
            
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
       
        st.title('Unique Delegators') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='DELEGATOR',
            color='DELEGATION_TYPE',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/99f380b5-8faa-4df8-bbd4-4a63e1f81045\">Query Link</a><br>",
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
        
    with cont :
        st.title('Delegated Amount') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='AMOUNT', 
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/99f380b5-8faa-4df8-bbd4-4a63e1f81045\">Query Link</a><br>",
            
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
            ])))
        st.plotly_chart(chart_daily,use_container_width=True)
        expander=st.expander("See The Analysis")
        expander.write("Chart shows The Weekly Delegated Amount For OP Token. \
             Date For The Analysis '2023-07-01' \
             . With the launch of OP token in June we saw a peak delegated amount in OP token after the hype of OP token we have seen a decrease in the delegated amount, but recently with the increase in the price of OP token it seems that \
                amount of OP delegated has started to increase again.  ")
        
    
        st.title('Weekly Delegations') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='DELEGATIONS', 
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/99f380b5-8faa-4df8-bbd4-4a63e1f81045\">Query Link</a><br>",
        )   
        chart_daily.update_xaxes(
        rangeslider_visible=False,
        
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])))
        st.plotly_chart(chart_daily,use_container_width=True)
        expander=st.expander("See The Analysis")
        expander.write("Chart shows The Weekly Delegation Transactions For Optimism. \
             Date For The Analysis '2023-07-01' \
             . We have seen highest increase in the delegations during the late of May and June  which was during the launch of the Optimism Token OP. \
               Number of delegations has dropped since then, but recently we can see that number of delegations has a trend of increase, one of the main reasons of this increase is \
                increase in the price of OP token.  ")
        
           



 
if options=='Daily Data':
    data(api1)
elif options=='Weekly Data':
    data(api1)
