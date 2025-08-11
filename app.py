import streamlit as st
import pandas as pd

# Importando as funções dos nossos módulos
from utils.data_loader import load_data
from utils.ui_components import render_sidebar, render_about_page
from utils.plots import (
    plot_evolucao_salarial,
    plot_top_cargos,
    plot_salario_histograma,
    plot_remoto_pie,
    plot_salario_mapa
)
# --- Configuração da Página ---
st.set_page_config(
    page_title="Dashboard de Salários de Dados",
    page_icon="📊",
    layout="wide",
)

# --- Carregamento dos Dados ---
df_original = load_data()

# --- Barra Lateral e Filtros ---
anos, senioridades, contratos, tamanhos = render_sidebar(df_original)

# --- Filtragem do DataFrame ---
df_filtrado = df_original[
    (df_original['ano'].isin(anos)) &
    (df_original['senioridade'].isin(senioridades)) &
    (df_original['contrato'].isin(contratos)) &
    (df_original['tamanho_empresa'].isin(tamanhos))
]

# --- Título Principal ---
st.title("🎲 Dashboard de Análise de Salários na Área de Dados")

# --- Abas de Navegação ---
tab_dashboard, tab_about = st.tabs(["📊 Dashboard Principal", "ℹ️ Sobre"])

# --- Aba 1: Dashboard Principal ---
with tab_dashboard:
    st.header("Métricas Gerais (Salário Anual em USD)")

    if not df_filtrado.empty:
        salario_medio = df_filtrado['usd'].mean()
        salario_maximo = df_filtrado['usd'].max()
        total_registros = df_filtrado.shape[0]
        cargo_mais_frequente = df_filtrado["cargo"].mode()[0]
    else:
        salario_medio, salario_maximo, total_registros, cargo_mais_frequente = 0, 0, 0, "N/A"

    # KPIs
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Salário médio", f"${salario_medio:,.0f}")
    col2.metric("Salário máximo", f"${salario_maximo:,.0f}")
    col3.metric("Total de registros", f"{total_registros:,}")
    col4.metric("Cargo mais frequente", cargo_mais_frequente)

    st.markdown("<hr>", unsafe_allow_html=True)
    st.header("Análises Visuais")

    # Gráfico de Evolução Salarial
    plot_evolucao_salarial(df_filtrado)

    # Gráficos em colunas
    col_graf1, col_graf2 = st.columns(2)
    with col_graf1:
        plot_top_cargos(df_filtrado)
    with col_graf2:
        plot_salario_histograma(df_filtrado)

    col_graf3, col_graf4 = st.columns(2)
    with col_graf3:
        plot_remoto_pie(df_filtrado)
    with col_graf4:
        plot_salario_mapa(df_filtrado)

    # Tabela de Dados Detalhados dentro de um Expander
    with st.expander("📂 Ver tabela de dados detalhados"):
        st.dataframe(df_filtrado)

# --- Aba 3: Sobre ---
with tab_about:
    render_about_page()
