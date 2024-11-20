import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

st.title('HELLOT WORLD AND RODRIGAMES')


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


st.title('PARTE DO TRAMPO DO GRINGO')

"""
Created on Sun Dec 25 19:20:54 2022

@author: Acer
"""

import streamlit as st
#import os
import numpy as np
import pickle
from prediction import predict

# MODEL_PATH = os.path.join(os.getcwd(),'best_model_covid.pkl')

#with open(MODEL_PATH,'rb') as file:
 #   model = pickle.load(file)


#%% STREAMLIT
with st.form("Patient's Form"):
    st.title("Prediction of Covid-19 Based on Symptoms")
    st.video("https://www.youtube.com/watch?v=U8r3oTVMtQ0", format="video/mp4") 
    # credit video: "Recognizing Day to Day Signs and Symptoms of Coronavirus" By FreeMedEducation YouTube channel
    st.header("Let's check if you have infected by Covid-19 virus!")
    st.write("0 = No,",
             "\n 1 = Yes.")
    breathing_problem = int(st.radio("Do you have breathing problem?", (0,1)))
    fever = int(st.radio("Do you experience fever?", (0,1)))
    dry_cough = int(st.radio("Do you get dry cough?", (0,1)))
    sore_throat = int(st.radio("Do you experience sore throat?", (0,1)))
    hyper_tension = int(st.radio("Do you encounter hyper tension for a few moment?", (0,1)))
    abroad_travel = int(st.radio("Do you travel abroad recently?", (0,1)))
    contact_with_covid_patient = int(st.radio("Do you meet anyone that is positive with Covid-19 recently?", (0,1)))
    attended_large_gathering = int(st.radio("Do you attend any gathering recently?", (0,1)))
    visited_public_exposed_places = int(st.radio("Do you visit any public exposed place?", (0,1)))
    family_working_in_public_exposed_places = int(st.radio("Do you have any family member that works in public exposed place?", (0,1)))
    

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("Breathing problem:",breathing_problem,
                 "Fever:",fever,
                 "Dry cough:",dry_cough,
                 "Sore throat:",sore_throat,
                 "Hypertension:",hyper_tension,
                 "Abroad travel:",abroad_travel,
                 "Contact with Covid-19:",contact_with_covid_patient,
                 "Attending large gathering:",attended_large_gathering,
                 "Visit public place:",visited_public_exposed_places,
                 "Family working in public place:",family_working_in_public_exposed_places)
        temp = np.expand_dims([breathing_problem,fever,dry_cough,sore_throat,
                               hyper_tension,abroad_travel,contact_with_covid_patient,
                               attended_large_gathering,visited_public_exposed_places,
                               family_working_in_public_exposed_places], axis=0)
        outcome = predict(temp)
        
        outcome_dict = {0:'Negative infection of Covid-19',
                        1:'Positive infection of Covid-19'}
        
        if outcome == 1:
            st.snow()
            st.markdown('**Oh...Oh...!** You are potentially infected with Covid-19 virus!')
            st.write("Please proceed to undergo testing for precaution whilst practice a good hygiene and seek medical attention if your symptoms worsen!")
            st.image("https://www.aicb.org.my/images/announcement/covid-19-positive/covwtd_01.jpg")
            # Credit pic: aicb.org.my website
        else:
            st.balloons()
            st.write("Hooray, you are not infected by Covid-19 virus. Please practice the SOP guidelines to combat Covid-19 disease from spreading!")
            st.image("https://cdn.who.int/media/images/default-source/health-topics/coronavirus/myth-busters/infographic-covid-19-transmission-and-protections-final2.jpg?sfvrsn=7fc5264a_2")
            # Credit pic: cdn.who.int/graphics website
        
