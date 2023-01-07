import streamlit  as st
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
# st.markdown("<img src='logos.png'> ", unsafe_allow_html=True)
# st.image('logo.png')
 
# Sidebar setup

#Sidebar navigation
st.sidebar.image('https://github.com/ernsahin/Optimismdash/blob/main/op/pages/logo.png?raw=true')
st.sidebar.title('Data Frame')
options = st.sidebar.radio('Select what you want to display:', [ 'Daily Data', 'Weekly Data'])
 

fig=go.Figure()
api1= pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/20bce94b-11bc-46bd-83bf-896b004af3a8/data/latest",orient='columns') 
api2=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/423c91f7-141e-4c00-8768-14f610551c4d/data/latest",orient='columns')
api3=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/a24671ce-7a08-4db6-a303-a309841b9dce/data/latest",orient='columns')
api4=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/908b6aa0-dff7-487c-9083-15fcd54a2d52/data/latest",orient='columns')
api5=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/1ef53c96-c455-4dfc-b9e6-86f1b1258e1d/data/latest",orient='columns')
api6=pd.read_json("https://node-api.flipsidecrypto.com/api/v2/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb/data/latest",orient='columns')

 

def stats():
    st.header("Welcome To The Optimism Megadashboard")
    st.text("In this megadashboard we will be looking at the ")
def data(dataframe) :
    transactions,transactions2=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Charts shows the transactions + their status. \
             Date For The Analysis '2023-07-01' \
             . During the Aug and September in most of the weeks number of transactions was below 1M but since the star of November number of transactions in Weekly has newer dropped below 1M also in December number of transactions has ended up above 4M three times.  ")
    with transactions : 
        st.title('Transactions') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='TXS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
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
       
        st.title('Status Of Transactions') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='TXS',
            color='STATUS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
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
    col3,col4=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Charts shows The Unique Users (People who send transaction )+ average gas fees. \
             Date For The Analysis '2023-07-01' \
             .Number of unique users has been increasing since the October while this number was below 200k users at weekly now we can see 400k unique users in a week which we could say users made 2x since October \
                Transaction Fees has dropped as well while more people uses Optimism Chain things like transaction fees + gas dropped.  ")
    with col3:   
       
        st.title('Unique Users') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='UNIQUE_USERS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    with col4:   
       
        st.title('Average Transaction Fee') 
        chart_daily = px.area(
            dataframe,
            x='DATE',
            y='AVG_TX_FEE',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
        
            
            
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
    col5,col6=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Chart shows Avg gas used + TPS . \
             Date For The Analysis '2023-07-01' \
             . While the gas use drops  tps increases, average gas used has dropped below the 5M at weekly which was above 15M at July also increase in the TPS has increased recently with most of the days of the week closes above 4 txs per second \
   ")
    with col5:   
       
        st.title('AVG Gas USED') 
        chart_daily = px.bar(
            dataframe,
            x='DATE',
            y='AVG_GAS_USED',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    with col6:   
       
        st.title('TPS') 
        chart_daily = px.scatter(
            dataframe,
            x='DATE',
            y='TPS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    expander=st.expander("See The Analysis")
    expander.write("Charts shows the transactions + their status. \
             Date For The Analysis '2023-07-01' \
             . During the Aug and September in most of the weeks number of transactions was below 1M but since the star of November number of transactions in Weekly has newer dropped below 1M also in December number of transactions has ended up above 4M three times.  ")
    with blocks : 
        st.title('Transactions') 
        chart_daily = px.bar(
            dataframe,
            x='DATE_WEEK',
            y='TXS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
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
            y='TXS',
            color='STATUS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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

    col3,col4=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Charts shows The Unique Users (People who send transaction )+ average gas fees. \
             Date For The Analysis '2023-07-01' \
             .Number of unique users has been increasing since the October while this number was below 200k users at weekly now we can see 400k unique users in a week which we could say users made 2x since October \
                Transaction Fees has dropped as well while more people uses Optimism Chain things like transaction fees + gas dropped.  ")
    with col3:   
       
        st.title('Unique Users') 
        chart_daily = px.bar(
            dataframe,
            x='DATE_WEEK',
            y='UNIQUE_USERS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    with col4:   
       
        st.title('Average Transaction Fee') 
        chart_daily = px.area(
            dataframe,
            x='DATE_WEEK',
            y='AVG_TX_FEE',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    col5,col6=st.columns(2)
    expander=st.expander("See The Analysis")
    expander.write("Chart shows Avg gas used + TPS . \
             Date For The Analysis '2023-07-01' \
             . While the gas use drops  tps increases, average gas used has dropped below the 5M at weekly which was above 15M at July also increase in the TPS has increased recently with most of the days of the week closes above 4 txs per second \
   ")
    with col5:   
       
        st.title('AVG Gas USED') 
        chart_daily = px.bar(
            dataframe,
            x='DATE_WEEK',
            y='AVG_GAS_USED',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    with col6:   
       
        st.title('TPS') 
        chart_daily = px.scatter(
            dataframe,
            x='DATE_WEEK',
            y='TPS',
            title =" Data: <a href=\"https://app.flipsidecrypto.com/velocity/queries/00e2ace4-d748-4a0d-8657-6e9bbc6a79bb\">Query Link</a><br>",
            
            
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
    data(api6)
elif options=='Weekly Data':
    data2(api6)

 
