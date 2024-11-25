import pandas as pd
import numpy as np
import pickle as pk
import streamlit as st

model=pk.load(open('model.pk1', 'rb'))

st.header('Car Price Prediction')

cars= pd.read_csv('C:/Users/ashfa/Desktop/car/car data.csv')

def get_brand_name(car_name):
    car_name=car_name.split(' ')[0]
    return car_name.strip(' ')
cars['CarName']=cars['CarName'].apply(get_brand_name)

symboling = st.slider('Select Symboling', 0, 3)
CarName = st.selectbox('Select Car Name', cars['CarName'].unique())
fueltype = st.selectbox('Select Fuel Type', cars['fueltype'].unique())
carbody = st.selectbox('Select Car Body', cars['carbody'].unique())
drivewheel = st.selectbox('Select Drive Wheel', cars['drivewheel'].unique())
enginelocation = st.selectbox('Select Engine Location', cars['enginelocation'].unique())
citympg = st.slider('Select City MPG', 10,50)
highwaympg = st.slider('Select Highway MPG', 10,50)
wheelbase = st.slider('Select Wheel Base', 85.5, 125.5)
carlength = st.slider('Select Car Length', 150.5, 220.5)
carwidth = st.slider('Select Car Width', 60.5, 75.5)
carheight = st.slider('Select Car Height', 40.5, 60.5)
curbweight = st.slider('Select Curb Weight', 1400, 4000)
enginetype = st.selectbox('Select Engine Type', cars['enginetype'].unique())
cylindernumber = st.selectbox('Select Cylinder Number', cars['cylindernumber'].unique())
enginesize = st.slider('Select Engine Size', 60, 310)
stroke = st.slider('Select Stroke', 1.55 ,5.55)
horsepower = st.slider('Select Horse Power', 50, 300)
peakrpm = st.slider('Select Peak RPM', 4000, 6000)

if st.button('Predict'):
    input_data_model= pd.DataFrame(
    [[symboling, CarName, fueltype,	carbody, drivewheel, enginelocation, citympg, highwaympg,
             wheelbase,	carlength, carwidth, carheight,	curbweight,	enginetype,	cylindernumber,	enginesize,	stroke,	horsepower,
             peakrpm]],
    columns=['symboling',	'CarName', 'fueltype',	'carbody',	'drivewheel',	'enginelocation',	'citympg',	'highwaympg',
             'wheelbase',	'carlength', 'carwidth',	'carheight',	'curbweight',	'enginetype',	'cylindernumber',	'enginesize',	'stroke',	'horsepower',
             'peakrpm']
)
    

    input_data_model['CarName'].replace(['alfa-romero', 'audi', 'bmw', 'chevrolet', 'dodge', 'honda',
       'isuzu', 'jaguar', 'maxda', 'mazda', 'buick', 'mercury',
       'mitsubishi', 'Nissan', 'nissan', 'peugeot', 'plymouth', 'porsche',
       'porcshce', 'renault', 'saab', 'subaru', 'toyota', 'toyouta',
       'vokswagen', 'volkswagen', 'vw', 'volvo'],
                       [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28], inplace=True)
    
    input_data_model['fueltype'].replace(['gas', 'diesel'], [1,2], inplace=True)

    input_data_model['carbody'].replace(['convertible', 'hatchback', 'sedan', 'wagon', 'hardtop'],
                          [1,2,3,4,5], inplace=True)
    
    input_data_model['drivewheel'].replace(['rwd', 'fwd', '4wd'],
                          [1,2,3], inplace=True)
    
    input_data_model['enginelocation'].replace(['front', 'rear'],
                          [1,2], inplace=True)
    
    input_data_model['enginetype'].replace(['dohc', 'ohcv', 'ohc', 'l', 'rotor', 'ohcf', 'dohcv'],
                          [1,2,3,4,5,6,7], inplace=True)
    
    input_data_model['cylindernumber'].replace(['four', 'six', 'five', 'three', 'twelve', 'two', 'eight'],
                          [4,6,5,3,12,2,8], inplace=True)
    

    price = model.predict(input_data_model)

    st.markdown('Car Price is going to be (in US Dollars):' + str(price[0]))
