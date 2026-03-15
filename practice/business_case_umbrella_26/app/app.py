import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import os

st.set_page_config(page_title="Прогноз погоды Москва", layout="wide")
st.title("Анализ погоды в Москве на 7 дней (Вариант 20)")

data_path = '/opt/airflow/data/clean_weather.csv'

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    
    st.write("### Очищенные данные с добавленным столбцом 'день недели'")
    st.dataframe(df)

    st.write("### График: Температура по дням недели")
    
    fig, ax = plt.subplots(figsize=(10, 5))
    # Чтобы график не сортировался по алфавиту, используем исходный порядок из df
    ax.plot(df['день недели'], df['temperature'], marker='o', color='orange', linewidth=2)
    ax.set_xlabel('День недели')
    ax.set_ylabel('Температура (°C)')
    ax.grid(True, linestyle='--', alpha=0.7)
    
    st.pyplot(fig)
else:
    st.warning("Данные еще не сгенерированы. Пожалуйста, запустите DAG в Airflow.")