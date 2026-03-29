import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

st.set_page_config(page_title="StockSense BI Dashboard", layout="wide")

st.title("Бизнес-кейс «StockSense»: Аналитика просмотров Википедии")

# Подключение к DWH (PostgreSQL)
@st.cache_resource
def init_connection():
    # URL для подключения внутри Docker сети
    db_url = "postgresql+psycopg2://airflow:airflow@wiki_results:5432/airflow"
    engine = create_engine(db_url)
    return engine

engine = init_connection()

# Загрузка данных
@st.cache_data(ttl=600)
def load_data():
    query = "SELECT * FROM pageview_counts ORDER BY datetime DESC"
    try:
        df = pd.read_sql(query, engine)
        return df
    except Exception as e:
        st.error(f"Ошибка подключения к БД: {e}")
        return pd.DataFrame()

df = load_data()

if df.empty:
    st.warning("Нет данных в БД. Запустите DAG в Airflow!")
else:
    df['datetime'] = pd.to_datetime(df['datetime'])
    
    st.subheader("Сырые данные (DWH)")
    st.dataframe(df.head(10))

    st.subheader("Динамика просмотров по компаниям")
    # Группировка данных для графика
    chart_data = df.groupby(['datetime', 'pagename'])['pageviewcount'].sum().reset_index()
    
    # Визуализация Plotly
    fig = px.line(chart_data, x='datetime', y='pageviewcount', color='pagename', markers=True,
                  title="Количество просмотров страниц Википедии (в час)")
    st.plotly_chart(fig, use_container_width=True)
    
    st.subheader("Суммарное количество просмотров")
    summary = df.groupby('pagename')['pageviewcount'].sum().reset_index().sort_values(by='pageviewcount', ascending=False)
    fig_bar = px.bar(summary, x='pagename', y='pageviewcount', color='pagename')
    st.plotly_chart(fig_bar, use_container_width=True)