import streamlit as st

def render_sidebar(df):
    """Renderiza a barra lateral com os filtros e retorna os valores selecionados."""
    st.sidebar.header("🔍 Filtros")

    # Filtro de Ano
    anos_disponiveis = sorted(df['ano'].unique())
    anos_selecionados = st.sidebar.multiselect("Ano", anos_disponiveis, default=anos_disponiveis)

    # Filtro de Senioridade
    senioridades_disponiveis = sorted(df['senioridade'].unique())
    senioridades_selecionadas = st.sidebar.multiselect("Senioridade", senioridades_disponiveis, default=senioridades_disponiveis)

    # Filtro por Tipo de Contrato
    contratos_disponiveis = sorted(df['contrato'].unique())
    contratos_selecionados = st.sidebar.multiselect("Tipo de Contrato", contratos_disponiveis, default=contratos_disponiveis)

    # Filtro por Tamanho da Empresa
    tamanhos_disponiveis = sorted(df['tamanho_empresa'].unique())
    tamanhos_selecionados = st.sidebar.multiselect("Tamanho da Empresa", tamanhos_disponiveis, default=tamanhos_disponiveis)

    return anos_selecionados, senioridades_selecionadas, contratos_selecionados, tamanhos_selecionados

def render_about_page():
    """Renderiza a página 'Sobre' com informações do projeto e do autor."""
    st.header("Sobre o Projeto")
    st.markdown("""
    Este dashboard foi desenvolvido como um projeto de portfólio para demonstrar 
    habilidades em análise de dados, visualização e desenvolvimento de aplicações web interativas com Python.
    
    **Funcionalidades Principais:**
    - **Dashboard Interativo:** Análise visual de salários com filtros dinâmicos.
    - **Análise de Tendências:** Gráfico de evolução da mediana salarial ao longo dos anos.
    - **Previsão com Machine Learning:** Uma ferramenta que estima faixas salariais com base nas características de um cargo, utilizando um modelo de regressão treinado.
    """)

    st.markdown("<hr>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🛠️ Tecnologias Utilizadas")
        st.markdown("""
        - **Python:** Linguagem principal.
        - **Pandas:** Para manipulação e análise dos dados.
        - **Streamlit:** Para a criação do dashboard.
        - **Plotly:** Para os gráficos interativos.
        - **Scikit-learn:** Para o modelo de Machine Learning.
        """)

    with col2:
        st.subheader("📄 Fonte dos Dados")
        st.markdown("""
        Os dados foram obtidos de uma fonte pública e contêm informações sobre salários 
        de profissionais de dados em diversos países e níveis de experiência.
        """)

    st.markdown("<hr>", unsafe_allow_html=True)

    st.subheader("👨‍💻 Sobre o Autor")
    st.markdown("""
    Este projeto foi criado pelo Desenvolvedor Front-End **Pedro Arthur Rodrigues**.
    
    Conecte-se comigo no LinkedIn!
    [Meu Perfil no LinkedIn](https://www.linkedin.com/in/parthurrod06/)
    """)
