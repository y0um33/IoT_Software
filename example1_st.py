import streamlit as st
import pandas as pd

st.title('Police Incident Reports from 2018 to 2020 in San Francisco')

df = pd.read_csv("Policev1.csv")

st.markdown(':rainbow[The data shown below belongs to incident report in the city of San Francisco, from the year 2018 to 2020, with details from each case sucas as date, day of the week, police district, neighborhood in which it happened, type of incident in category and subcategory, exact location and resolution]')

mapa = pd.DataFrame()
mapa['Date'] = df['Incident Date']
mapa['Day'] = df['Incident Day of Week']
mapa['Police District'] = df['Police District']
mapa['Neighborhood'] = df['Analysis Neighborhood']
mapa['Incident Category'] = df['Incident Category']
mapa['Incident Subcategory'] = df['Incident Subcategory']
mapa['Resolution'] = df['Resolution']
mapa['lat'] = df['Latitude']
mapa['lon'] = df['Longitude']
mapa = mapa.dropna()
