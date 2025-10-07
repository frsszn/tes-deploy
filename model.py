import streamlit as st
import pandas as pd
import numpy as np
import os
import pickle
import json

def predict():
    # Load all files

    with open('model_lin_reg.pkl', 'rb') as file_1:
        model_lin_reg = pickle.load(file_1)

    with open('model_scaler.pkl', 'rb') as file_2:
        model_scaler = pickle.load(file_2)

    with open('model_encoder.pkl','rb') as file_3:
        model_encoder = pickle.load(file_3)

    with open('list_num_cols.txt', 'r') as file_4:
        list_num_cols = json.load(file_4)

    with open('list_cat_cols.txt', 'r') as file_5:
        list_cat_cols = json.load(file_5)

    with st.form(key = 'player'):

        name = st.text_input("Masukan Nama pemain", placeholder='Prabowo Subianto')
        st.write("___")
        age = st.number_input("Masukan Umur Pemain", placeholder='73')
        height = st.number_input("Masukan Tinggi Pemain", placeholder='160')
        weight = st.number_input("Masukan Berat Pemain", placeholder='100')
        price = st.number_input("Masukan Harga Pemain (Euro)", placeholder='1000000')
        st.write("___")
        awr = st.selectbox('Attacking Work Rate Pemain', ("Low", "Medium", "High"))
        dwr = st.selectbox('Defending Work Rate Pemain', ("Low", "Medium", "High"))
        st.write("___")
        pace = st.slider("Masukan Stat Pace Pemain", min_value=0, max_value=99, value=50)
        shooting = st.slider("Masukan Stat Shooting Pemain", min_value=0, max_value=99, value=50)
        passing = st.slider("Masukan Stat Passing Pemain", min_value=0, max_value=99, value=50)
        dribbling = st.slider("Masukan Stat Dribbling Pemain", min_value=0, max_value=99, value=50)
        defending = st.slider("Masukan Stat Defending Pemain", min_value=0, max_value=99, value=50)
        physical= st.slider("Masukan Stat Physical Pemain", min_value=0, max_value=99, value=50)

        


        data_inf = {
            'Name': name,
            'Age': age,
            'Height': height,
            'Weight': weight,
            'Price': price,
            'AttackingWorkRate': awr,
            'DefensiveWorkRate': dwr,
            'PaceTotal': pace,
            'ShootingTotal': shooting,
            'PassingTotal': passing,
            'DribblingTotal': dribbling,
            'DefendingTotal': defending,
            'PhysicalityTotal': physical
        }
        data_inf = pd.DataFrame([data_inf])

        submit = st.form_submit_button('Predict')

    data_inf_num = data_inf[list_num_cols]
    data_inf_cat = data_inf[list_cat_cols]


    # Feature Scaling and Feature Encoding

    ## Feature Scaling
    data_inf_num_scaled = model_scaler.transform(data_inf_num)

    ## Feature Encoding
    data_inf_cat_encoded = model_encoder.transform(data_inf_cat)

    ## Concate
    data_inf_final = np.concatenate([data_inf_num_scaled, data_inf_cat_encoded], axis=1)

    # Predict using Linear Regression

    y_pred_inf = model_lin_reg.predict(data_inf_final)
    st.write('# Prediction', round(y_pred_inf[0], 2))

if __name__ == '__main__':
    predict()
