# Este módulo é responsável por carregar os dados utilizados no dashboard.
# Ele utiliza o pandas para leitura de CSV e o Streamlit para cache de dados.

import pandas as pd
import streamlit as st

# Esta função carrega o dataset de salários a partir de uma URL remota.
@st.cache_data
def load_data():
    df = pd.read_csv("https://raw.githubusercontent.com/vqrca/dashboard_salarios_dados/refs/heads/main/dados-imersao-final.csv")
    return df