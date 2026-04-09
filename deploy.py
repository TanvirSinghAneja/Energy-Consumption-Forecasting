import streamlit as st

st.set_page_config(layout="wide")
st.title('Energy Forecasting')
tab1,tab2,tab3,tab4=st.tabs(['EDA','Sesonality','Models','Forecasting'])

# Tab 1 Exploratory Data Analysis
with tab1:
  st.header('Exploratory Data Analysis')
  st.subheader('Trend Analysis')
  st.image('1_trends.png')
  st.image('1_season_holiday.png')
  st.subheader('Usage Distribution')
  st.image('1_hist.png')
  with st.expander('Assumption Taken'):
    col_l,col_r=st.columns([1,1])
    with col_l:
      st.subheader("U.S. Seasons")
      st.markdown("""
      | Season | Start Date | End Date |
      | :--- | :--- | :--- |
      | **Spring** | March 21 | June 20 |
      | **Summer** | June 21 | September 22 |
      | **Autumn** | September 23 | December 20 |
      | **Winter** | December 21 | March 20 |

      *Source: [SassyFeeds](https://sassyfeeds.com/seasons-and-dates-in-the-us-a-complete-guide-to-weather-changes-across-the-year/)*
      """)
    with col_r:
      st.subheader("U.S. Federal Holidays")
      st.markdown("""
      | Holiday | Date / Occurrence |
      | :--- | :--- |
      | **New Year's Day** | January 1 |
      | **Martin Luther King Jr. Day** | 3rd Monday of January |
      | **Inauguration Day** | January 20 (Every 4 years) |
      | **Washington’s Birthday** | 3rd Monday of February |
      | **Memorial Day** | Last Monday of May |
      | **Juneteenth** | June 19 |
      | **Independence Day** | July 4 |
      | **Labor Day** | 1st Monday of September |
      | **Columbus Day** | 2nd Monday of October |
      | **Veterans Day** | November 11 |
      | **Thanksgiving Day** | 4th Thursday of November |
      | **Christmas Day** | December 25 |

      *Source: [USA.gov](https://www.usa.gov/holidays)*
    """)

# Tab 2 Seasonal Decomposition
with tab2:
  st.header('Seasonal Decomposition')
  st.image('2_seasonal_decomp.png')
  st.header('Stationary Test')
  st.image('2_stationary.png')
  col_l,col_r=st.columns([1,3])
  with col_l:
    st.subheader("Dikcey Fuller Test")
    st.markdown("""
    | Metrics | Value |
    | :--- | :--- |
    | **Test Stats** | -1.132127e+01 |
    | **P Value** | 1.172567e-20 |
    | **Lags Used** | 5.200000e+01 |
    | **No Of Obs** | 3.498700e+04 |
    | **Crtical Value (1%)** | -3.430537e+00 |
    | **Crtical Value (5%)** | -2.861623e+00 |
    | **Crtical Value (10%)** | -2.566814e+00 |
    """)
  with col_r:
    st.subheader("ACF and PACF Curves")
    st.image('2_acf_pacf.png')

# Tab 3 Models
with tab3:
  st.header('Models Build')
  st.image('3_overall.png')
  st.write('Since the Data is **Stationary** we will just be taking the last **5 Years** of data to build the Model, to reduce time and capture trends and pattern from recent data.')
  col_i,col_t=st.columns([1,1])
  with col_i:
    st.subheader('ARIMA')
    st.image('3_arima.png')
  with col_t:
    st.subheader('Metrics')
    st.markdown('''
    | Metrics | Value |
    | :--- | :--- |
    | **Mean Absolute Error** | 785.5 |
    | **Mean Absolute Percentage Error** | 0.14 |
    | **Mean Squared Error** | 1001772.32 |
    | **Root Mean Squared Error** | 1000.89 |
    | **R2 Score** | -0.01 |
    ''')
    st.write('**ARIMA** model is usually not good for Seasonal Data so we will not be considering this.')
  st.divider()
  col_i,col_t=st.columns([1,1])
  with col_i:
    st.subheader('SARIMAX')
    st.image('3_sarimaz.png')
  with col_t:
    st.subheader('Metrics')
    st.markdown('''
    | Metrics | Value |
    | :--- | :--- |
    | **Mean Absolute Error** | 2310.22 |
    | **Mean Absolute Percentage Error** | 0.39 |
    | **Mean Squared Error** | 7300740.72 |
    | **Root Mean Squared Error** | 2701.99 |
    | **R2 Score** | -6.4 |
    ''')
    st.write('**SARIMAX** is good for seasonal data but has performed worser that ARIMA. Thus we will not be using this too.')
  st.divider()
  col_i,col_t=st.columns([3,1])
  with col_i:
    st.subheader('Simple RNN')
    st.image('3_rnn.png')
  with col_t:
    st.subheader('Metrics')
    st.markdown('''
    | Metrics | Base | Final |
    | :--- | :--- | :--- |
    | **Mean Absolute Error** | 383.58 | 73.54 |
    | **Mean Absolute Percentage Error** | 0.07 | 0.01 |
    | **Mean Squared Error** | 252052.81 | 9257.62 |
    | **Root Mean Squared Error** | 502.05 | 96.22 |
    | **R2 Score** | 0.74 | 0.99 |
    ''')
    st.write('**Simple RNN** outperformed other model but was not as effecient as LSTM.')
  st.divider()
  col_i,col_t=st.columns([3,1])
  with col_i:
    st.subheader('GRU')
    st.image('3_gru.png')
  with col_t:
    st.subheader('Metrics')
    st.markdown('''
    | Metrics | Base | Final |
    | :--- | :--- | :--- |
    | **Mean Absolute Error** | 383.58 | 77.65 |
    | **Mean Absolute Percentage Error** | 0.07 | 0.01 |
    | **Mean Squared Error** | 252052.81 | 10526.62 |
    | **Root Mean Squared Error** | 502.05 | 102.6 |
    | **R2 Score** | 0.74 | 0.99 |
    ''')
    st.write('**GRU** outperformed all other model but was not as good as GRU. SO we will not be taking it.')
  st.divider()
  col_i,col_t=st.columns([3,1])
  with col_i:
    st.subheader('LSTM')
    st.image('3_lstm.png')
  with col_t:
    st.subheader('Metrics')
    st.markdown('''
    | Metrics | Base | Final |
    | :--- | :--- | :--- |
    | **Mean Absolute Error** | 383.58 | 71.69 |
    | **Mean Absolute Percentage Error** | 0.07 | 0.01 |
    | **Mean Squared Error** | 252052.81 | 8528.98 |
    | **Root Mean Squared Error** | 502.05 | 92.35 |
    | **R2 Score** | 0.74 | 0.99 |
    ''')
    st.write('**LSTM** outperformed all other model as it Has the least MAE even compared to its base model. So we will choose it for forecasting.')

# Tab 4 Forecasting
with tab4:
  import pandas as pd
  import matplotlib.pyplot as plt
  df=pd.read_csv('forecast.csv',parse_dates=True,index_col=0)
  df['date']=pd.to_datetime(df.index.normalize())
  df['day']=df.index.day
  df['day_name']=df.index.day_name()
  df['hour']=df.index.hour
  col_l,col_r=st.columns([3,1])
  with col_r:
    st.subheader('Select')
    opt=st.radio('Choose',['Overall','Hourly','Daily','Weekly'])
  with col_l:
    if opt=='Overall':
      st.subheader('Overall Forecast for Next Month')
      # st.image('3_forecast.png')
      df['use'].plot()
      plt.title('Overall Forecast')
      plt.xlabel('Datetime')
      plt.ylabel('Energy Consumption')
      for x in range(len(df['use'])):
        mm=df['use'].iloc[x]
        if mm==df['use'].min() or mm==df['use'].max():
          plt.text(df.index[x],mm,round(mm),ha='center',va='bottom')
      st.pyplot(plt)
    elif opt=='Hourly':
      st.subheader('Hourly Forecast for Next Month')
      hr=df.groupby('hour')['use'].agg(['mean'])
      plt.plot(hr.index,hr['mean'])
      plt.title('Hourly Forecast')
      plt.xlabel('Datetime')
      plt.ylabel('Energy Consumption')
      for x in range(len(hr)):
        mm=hr['mean'].iloc[x]
        if mm==hr['mean'].min() or mm==hr['mean'].max():
          plt.text(hr.index[x],mm,round(mm),ha='center',va='bottom')
      st.pyplot(plt)
    elif opt=='Daily':
      st.subheader('Daily Forecast for Next Month')
      dy=df.groupby('day')['use'].agg(['mean'])
      plt.plot(dy.index,dy['mean'])
      plt.title('Daily Average Forecast')
      plt.xlabel('Date')
      plt.ylabel('Energy Consumption')
      for x in range(len(dy)):
        mm=dy['mean'].iloc[x]
        if mm==dy['mean'].min() or mm==dy['mean'].max():
          plt.text(dy.index[x],mm,round(mm),ha='center',va='bottom')
      st.pyplot(plt)
    elif opt=='Weekly':
      st.subheader('Weekly Forecast for Next Month')
      wk=df.groupby('day_name')['use'].agg(['mean'])
      wk=wk.reindex(['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'])
      plt.plot(wk.index,wk['mean'])
      plt.title('Average Forecast by Weekday')
      plt.xlabel('Day')
      plt.ylabel('Energy Consumption')
      for x in range(len(wk)):
        mm=wk['mean'].iloc[x]
        if mm==wk['mean'].min() or mm==wk['mean'].max():
          plt.text(wk.index[x],mm,round(mm),ha='center',va='bottom')
      st.pyplot(plt)
