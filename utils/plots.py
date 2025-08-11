import plotly.express as px
import streamlit as st

def plot_evolucao_salarial(df):
    """Gera o gráfico de linhas com a evolução da mediana salarial por ano."""
    if not df.empty:
        # Agrupa por ano e senioridade, calcula a mediana dos salários
        df_evolucao = df.groupby(['ano', 'senioridade'])['usd'].median().reset_index()

        grafico = px.line(
            df_evolucao,
            x='ano',
            y='usd',
            color='senioridade',
            title='Evolução da Mediana Salarial por Senioridade',
            labels={'usd': 'Mediana Salarial Anual (USD)', 'ano': 'Ano', 'senioridade': 'Senioridade'},
            markers=True, # Adiciona marcadores nos pontos de dados
            template='plotly_white'
        )
        grafico.update_layout(title_x=0.1)
        st.plotly_chart(grafico, use_container_width=True)
    else:
        st.warning("Nenhum dado para exibir no gráfico de evolução salarial.")

def plot_top_cargos(df):
    """Gera o gráfico de barras com o top 10 cargos por salário médio."""
    if not df.empty:
        top_cargos = df.groupby('cargo')['usd'].mean().nlargest(10).sort_values(ascending=True).reset_index()
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

def plot_salario_histograma(df):
    """Gera o histograma com a distribuição de salários."""
    if not df.empty:
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

def plot_remoto_pie(df):
    """Gera o gráfico de pizza com a proporção de trabalho remoto."""
    if not df.empty:
        remoto_contagem = df['remoto'].value_counts().reset_index()
        remoto_contagem.columns = ['tipo_trabalho', 'quantidade']
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

def plot_salario_mapa(df):
    """Gera o mapa coroplético com o salário médio de Cientista de Dados por país."""
    if not df.empty:
        df_ds = df[df['cargo'] == 'Data Scientist']
        if not df_ds.empty:
            media_ds_pais = df_ds.groupby('residencia_iso3')['usd'].mean().reset_index()
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
