# utils/ui_components.py

# Este módulo contém funções para renderizar componentes da interface do usuário no Streamlit,
# como a barra lateral de filtros e a página 'Sobre' do dashboard.

import streamlit as st

# Função para renderizar a barra lateral de filtros.
# Recebe o DataFrame original para extrair as opções de filtro e retorna os valores selecionados.
def render_sidebar(df):
    
    st.sidebar.header("🔍 Filtros")

    # Filtro por Ano
    anos_disponiveis = sorted(df['ano'].unique())
    anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

    # Filtro por Senioridade
    senioridades_disponiveis = sorted(df['senioridade'].unique())
    senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

    # Filtro por Tipo de Contrato
    contratos_disponiveis = sorted(df['contrato'].unique())
    contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

    # Filtro por Tamanho da Empresa
    tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
    tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

    return anos_selecionados, senioridades_selecionadas, contratos_selecionados, tamanhos_selecionados

# Função para renderizar o conteúdo da página 'Sobre' o projeto.
def render_about_page():
    
    st.header("Sobre o Projeto")
    st.markdown("""
    Este dashboard foi desenvolvido como um projeto de portfólio para demonstrar 
    habilidades em análise de dados, visualização e desenvolvimento de aplicações web interativas com Python.
    
    **Funcionalidades Principais:**
    - **Dashboard Interativo:** Análise visual de salários com filtros dinâmicos.
    - **Análise de Tendências:** Gráfico de evolução da mediana salarial ao longo dos anos.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        # Seção de Tecnologias Utilizadas
        st.subheader("🛠️ Tecnologias Utilizadas")
        st.markdown("""
        - **Python:** Linguagem principal.
        - **Pandas:** Para manipulação e análise dos dados.
        - **Streamlit:** Para a criação do dashboard.
        - **Plotly:** Para os gráficos interativos.
        """)

    with col2:
        # Seção de Fonte dos Dados
        st.subheader("📄 Fonte dos Dados")
        st.markdown("""
        Os dados foram obtidos de uma fonte pública e contêm informações sobre salários 
        de profissionais de dados em diversos países e níveis de experiência.
        """)

    st.markdown("<hr>", unsafe_allow_html=True)

    # Seção Sobre o Autor
    st.subheader("👨‍💻 Sobre o Autor")
    st.markdown("""
    Este projeto foi criado pelo Desenvolvedor Front-End **Pedro Arthur Rodrigues**.
    
    Conecte-se comigo no LinkedIn!
    [Meu Perfil no LinkedIn](https://www.linkedin.com/in/parthurrod06/)
    """)