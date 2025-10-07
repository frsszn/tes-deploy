import streamlit as st
import eda, model

with st.sidebar:
        st.title('Page Navigation')
        # input
        page = st.radio('Page', ['EDA', 'Model Demo'])

        st.write('# About')
        st.write('''
                 Page ini adalah informasi data dan demo dari model prediksi player rating''')
        
if page == 'EDA':
        eda.first()

else:
        model.predict()
