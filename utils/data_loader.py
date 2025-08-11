import pandas as pd
import streamlit as st

@st.cache_data
def load_data():
    """
    Carrega os dados do CSV, realiza traduções e retorna um DataFrame limpo.
    O decorador @st.cache_data garante que os dados sejam carregados apenas uma vez.
    """
    df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
    return df
