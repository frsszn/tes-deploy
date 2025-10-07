import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

def first():
    st.title("FIFA Data Exploration")
    st.image("https://img.allfootballapp.com/www/M00/5A/6D/720x-/-/-/rB8ApF2LH-KAUokdAAF7KSeQN0w012.jpg.webp", caption='Source: google.com')

    st.markdown("## Latar Belakang")

    st.markdown('''Menurut laporan FIFA 2022, jumlah pemain sepakbola pada tahun 2021 kurang lebih sebanyak 130.000 pemain. Namun, dalam dataset yang digunakan pada kali ini, hanya mencakup 20.000 pemain saja. Project kali ini bertujuan untuk memprediksi rating pemain FIFA 2022 sehingga semua pemain sepak bola profesional dapat diketahui ratingnya dan tidak menutup kemungkinan untuk lahirnya talenta/wonderkid baru.

    Project ini akan dibuat menggunakan algoritma Linear Regresison dan akan dievaluasi dengan menggunakan metrics MAE (Mean Absolute Error).''')

    st.markdown("## Dataset")
    st.markdown('''Rating dan atribut pemain FIFA 2022 yang diambil dari web Sofifa.com''')



    data = pd.read_csv('https://raw.githubusercontent.com/FTDS-learning-materials/phase-1/refs/heads/v2.3/w1/P1W1D1PM%20-%20Machine%20Learning%20Problem%20Framing.csv')
    data.rename(columns={'ValueEUR': 'Price', 'Overall': 'Rating'}, inplace=True)
    st.write(data)

    st.markdown("## Exploratory Data Analysis")
    st.markdown("### Player Rating Distribution")

    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data['Rating'], kde=True, bins=30)
    plt.title('Histogram of Rating')
    st.pyplot(fig)

    # Scatterplot Weight vs Height
    st.markdown("### Weight vs Height Distribution")
    fig1 = px.scatter(
        data, 
        x='Weight', 
        y='Height', 
        title='Weight vs Height',
        color_discrete_sequence=['#EF553B'],
    )
    fig1.update_layout(
        width=900, height=400,
        title_x=0.5,
    )
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### Player Stat Distribution")

    namakolom = data.columns
    option = st.selectbox(
        'Pick a Stat:',
        ('PaceTotal', 'ShootingTotal', 'PassingTotal', 'DribblingTotal', 'DefendingTotal', 'PhysicalityTotal')
    )

    fig = plt.figure(figsize=(16, 5))
    sns.histplot(data[option], kde=True, bins=30)
    plt.title(f'Histogram of {option}')
    st.pyplot(fig)

if __name__ == '__main__':
    first()

