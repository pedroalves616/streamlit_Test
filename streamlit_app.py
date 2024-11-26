import streamlit as st
import pandas as pd
import numpy as np

#img teste
from streamlit_extras.image_in_tables import table_with_images

def example(df: pd.DataFrame):
    st.caption("Input dataframe (notice 'Flag' column is full of URLs)")
    st.write(df)
    df_html = table_with_images(df=df, url_columns=("Flag",))
    st.caption("Ouput")
    st.markdown(df_html, unsafe_allow_html=True)

    
st.title('Uber pickups in NYC')

st.title('HELLOT WORLD ')
st.title('teste asdasdasdasd ')


DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
         'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text('Loading data...')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('Loading data...done!')

@st.cache_data

def load_data(nrows):

    data_load_state.text("Done! (using st.cache_data)")

st.subheader('Raw data')
st.write(data)


        
