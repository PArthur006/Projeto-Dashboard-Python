# Este módulo contém funções para gerar os gráficos utilizados no dashboard.
# Cada função recebe um DataFrame e renderiza um gráfico Plotly Express no Streamlit.

import plotly.express as px
import streamlit as st

# Função para plotar a evolução salarial por senioridade ao longo dos anos.
def plot_evolucao_salarial(df):
    
    if not df.empty:
        # Agrupa os dados para calcular a mediana salarial por ano e senioridade.
        df_evolucao = df.groupby(['ano', 'senioridade'])['usd'].median().reset_index()

        # Cria o gráfico de linha usando Plotly Express.
        grafico = px.line(
            df_evolucao,
            x='ano',
            y='usd',
            color='senioridade',
            title='Evolução da Mediana Salarial por Senioridade',
            labels={'usd': 'Mediana Salarial Anual (USD)', 'ano': 'Ano', 'senioridade': 'Senioridade'},
            markers=True, 
            template='plotly_white'
        )
        grafico.update_layout(title_x=0.1)
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de evolução salarial.")

# Função para plotar os top 10 cargos por salário médio.
def plot_top_cargos(df):
    
    if not df.empty:
        top_cargos = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
        # Cria o gráfico de barras usando Plotly Express.
        grafico = px.bar(
            top_cargos,
            x='usd',
            y='cargo',
            orientation='h',
            title="Top 10 cargos por salário médio",
            labels={'usd': 'Média salarial anual (USD)', 'cargo': ''},
            template='plotly_white'
        )
        grafico.update_layout(title_x=0.1, yaxis={'categoryorder':'total ascending'})
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de cargos.")

# Função para plotar o histograma da distribuição de salários.
def plot_salario_histograma(df):
    
    if not df.empty:
        # Cria o histograma usando Plotly Express.
        grafico = px.histogram(
            df,
            x='usd',
            nbins=30,
            title="Distribuição de salários anuais",
            labels={'usd': 'Faixa salarial (USD)', 'count': ''},
            template='plotly_white'
        )
        grafico.update_layout(title_x=0.1)
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de distribuição.")

# Função para plotar um gráfico de pizza da proporção de tipos de trabalho (remoto/presencial).
def plot_remoto_pie(df):
    
    if not df.empty:
        remoto_contagem = df['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
        # Cria o gráfico de pizza usando Plotly Express.
        grafico = px.pie(
            remoto_contagem,
            names='tipo_trabalho',
            values='quantidade',
            title='Proporção dos tipos de trabalho',
            hole=0.5,
            template='plotly_white'
        )
        grafico.update_traces(textinfo='percent+label')
        grafico.update_layout(title_x=0.1)
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico dos tipos de trabalho.")

# Função para plotar um mapa coroplético do salário médio de Cientistas de Dados por país.
def plot_salario_mapa(df):
    
    if not df.empty:
        df_ds = df[df['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
            # Cria o mapa coroplético usando Plotly Express.
            grafico = px.choropleth(
                media_ds_pais,
                locations='residencia_iso3',
                color='usd',
                color_continuous_scale='rdylgn',
                title='Salário médio de Cientista de Dados por país',
                labels={'usd': 'Salário médio (USD)', 'residencia_iso3': 'País'},
                template='plotly_white'
            )
            grafico.update_layout(title_x=0.1)
            st.plotly_chart(grafico, use_container_width=True)
        else:
            st.warning("Nenhum dado de 'Data Scientist' para exibir no mapa.")
    else:
        st.warning("Nenhum dado para exibir no gráfico de países.")