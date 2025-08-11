# Anotações do Curso: Análise de Dados com Python e Pandas

Este documento resume os principais comandos e técnicas abordados durante o curso, utilizando um dataset de salários da área de tecnologia como exemplo.

---

## Aula 1: Carregamento e Exploração de Dados

Nesta aula, aprendemos a carregar dados de uma fonte externa, traduzir colunas e valores para um formato mais amigável e realizar uma inspeção inicial para entender a estrutura do nosso DataFrame.

### Código Completo da Aula 1

```python
# Importação de bibliotecas
import pandas as pd

# Carrega o DataFrame a partir de um arquivo CSV online
df = pd.read_csv("https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv")

# Dicionário para renomear as colunas para o português
renomear_colunas = {
    'work_year': 'ano',
    'experience_level': 'senioridade',
    'employment_type': 'contrato',
    'job_title': 'cargo',
    'salary': 'salario',
    'salary_currency': 'moeda',
    'salary_in_usd': 'usd',
    'employee_residence': 'residencia',
    'remote_ratio': 'remoto',
    'company_location': 'empresa',
    'company_size': 'tamanho_empresa'
}
df.rename(columns=renomear_colunas, inplace=True)

# Dicionários de tradução para os valores das colunas categóricas
traducao_senioridade = {'SE': 'Sênior', 'MI': 'Pleno', 'EN': 'Júnior', 'EX': 'Executivo'}
traducao_contrato = {'FT': 'Tempo Integral', 'PT': 'Meio Período', 'CT': 'Contrato', 'FL': 'Freelance'}
traducao_remoto = {100: 'Remoto', 50: 'Híbrido', 0: 'Presencial'}
traducao_tamanho_empresa = {'L': 'Grande', 'M': 'Média', 'S': 'Pequena'}

# Aplica as traduções usando o método .map()
df['senioridade'] = df['senioridade'].map(traducao_senioridade)
df['contrato'] = df['contrato'].map(traducao_contrato)
df['remoto'] = df['remoto'].map(traducao_remoto)
df['tamanho_empresa'] = df['tamanho_empresa'].map(traducao_tamanho_empresa)

# Comandos de inspeção (úteis para verificar o resultado)
print("--- Primeiras 5 linhas do DataFrame: ---")
print(df.head())
print("
--- Informações gerais do DataFrame: ---")
df.info()
print(f"
--- O DataFrame tem {df.shape[0]} linhas e {df.shape[1]} colunas. ---")
```

### Métodos Essenciais da Aula 1

-   **`pd.read_csv()`**: Carrega dados de um arquivo CSV para um DataFrame.
-   **`.rename(columns=dicionario, inplace=True)`**: Renomeia as colunas do DataFrame. O `inplace=True` modifica o DataFrame original.
-   **`.map(dicionario)`**: Substitui cada valor em uma coluna (Series) pelo seu correspondente no dicionário.
-   **`.head()`**: Exibe as primeiras linhas.
-   **`.info()`**: Mostra um resumo técnico (tipos de dados, valores nulos).
-   **`.shape`**: Retorna uma tupla com as dimensões (linhas, colunas).

---

## Aula 2: Limpeza e Preparação dos Dados

O foco desta aula foi tratar dados ausentes e otimizar os tipos de dados (`dtypes`) para garantir a qualidade e eficiência da análise.

### Código Completo da Aula 2

```python
# O DataFrame 'df' vem da Aula 1

# A função .dropna() remove linhas que contêm valores nulos (NaN).
df_limpo = df.dropna()

# O método .assign() permite criar ou modificar múltiplas colunas de uma vez.
# Aqui, ele está sendo usado para converter os tipos de dados (dtypes).
df_limpo = df_limpo.assign(
    ano = df_limpo['ano'].astype('int64'),
    # Exemplo de como otimizar outras colunas (não presente no script original, mas boa prática)
    remoto = df_limpo['remoto'].astype('category'),
    tamanho_empresa = df_limpo['tamanho_empresa'].astype('category')
)

# Comandos de inspeção
print("--- Informações do DataFrame após limpeza e otimização: ---")
df_limpo.info()
```

### Métodos Essenciais da Aula 2

-   **`.dropna()`**: Remove linhas com valores nulos (NaN).
-   **`.assign()`**: Permite criar ou modificar colunas de forma encadeada.
-   **`.astype()`**: Converte o tipo de dado de uma coluna. Usar `'category'` para colunas de texto com poucos valores únicos é uma ótima forma de otimizar memória.

---

## Aula 3: Visualização de Dados

Nesta aula, exploramos como criar gráficos para contar histórias com os dados, utilizando as bibliotecas Matplotlib, Seaborn e Plotly.

### Configuração do Ambiente

Para exibir gráficos em janelas interativas, especialmente com Matplotlib, pode ser necessário configurar o backend. Para salvar arquivos com Plotly, a biblioteca `kaleido` pode ser necessária.

```python
import matplotlib
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# Configura o backend do Matplotlib (opcional, dependendo do ambiente)
# matplotlib.use('TkAgg')

# Instalação do Kaleido (necessário para salvar imagens com Plotly)
# !pip install kaleido
```

### Gráficos com Matplotlib e Seaborn (Estáticos)

#### 1. Gráfico de Barras: Distribuição de Senioridade (Matplotlib)
Mostra a contagem de cada nível de senioridade.

```python
plt.figure(figsize=(10, 6))
ax = df_limpo['senioridade'].value_counts().plot(kind='bar', color='skyblue')
ax.set_title('Distribuição de Senioridade', fontsize=16)
ax.set_xlabel('Nível de Senioridade', fontsize=12)
ax.set_ylabel('Número de Profissionais', fontsize=12)
ax.tick_params(axis='x', rotation=45) # Rotaciona os rótulos para melhor leitura

# Adiciona os rótulos de dados em cada barra
for p in ax.patches:
    ax.annotate(str(p.get_height()), (p.get_x() + p.get_width() / 2., p.get_height()),
                ha='center', va='center', xytext=(0, 5), textcoords='offset points')

plt.tight_layout()
plt.show()
```

#### 2. Gráfico de Barras: Salário Médio por Senioridade (Seaborn)
Compara o salário médio em USD para cada nível de senioridade.

```python
ordem = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=True).index
plt.figure(figsize=(8, 5))
sns.barplot(data=df_limpo, x='senioridade', y='usd', order=ordem, palette='viridis', hue='senioridade', legend=False)
plt.title('Salário Médio por Nível de Senioridade', fontsize=14)
plt.xlabel('Senioridade', fontsize=12)
plt.ylabel('Salário Médio Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()
```

#### 3. Histograma: Distribuição de Salários (Seaborn)
Mostra a frequência dos salários anuais.

```python
plt.figure(figsize=(10, 5))
sns.histplot(df_limpo['usd'], bins=50, kde=True, color='skyblue')
plt.title('Distribuição de Salários Anuais', fontsize=14)
plt.xlabel('Salário Anual (USD)', fontsize=12)
plt.ylabel('Frequência', fontsize=12)
plt.tight_layout()
plt.show()
```

#### 4. Boxplot: Salários por Senioridade (Seaborn)
Exibe a distribuição (mediana, quartis, outliers) dos salários para cada senioridade.

```python
ordem_senioridade = ['Júnior', 'Pleno', 'Sênior', 'Executivo']
plt.figure(figsize=(8, 5))
sns.boxplot(x='senioridade', y='usd', data=df_limpo, order=ordem_senioridade, palette='Set2', hue='senioridade', legend=False)
plt.title('Boxplot de Salários Anuais por Nível de Senioridade', fontsize=14)
plt.xlabel('Nível de Senioridade', fontsize=12)
plt.ylabel('Salário Anual (USD)', fontsize=12)
plt.tight_layout()
plt.show()
```

### Gráficos com Plotly (Interativos)

#### 1. Gráfico de Rosca: Proporção dos Tipos de Trabalho
Gráfico interativo mostrando a proporção de trabalho remoto, híbrido e presencial.

```python
remoto_contagem = df_limpo['remoto'].value_counts().reset_index()
remoto_contagem.columns = ['tipo_trabalho', 'quantidade']

fig = px.pie(remoto_contagem,
             names='tipo_trabalho',
             values='quantidade',
             title='Proporção dos Tipos de Trabalho',
             hole=0.5)
fig.update_traces(textposition='inside', textinfo='percent+label')

# Para visualizar:
# fig.show()
# Para salvar como HTML interativo:
fig.write_html("grafico_proporcao_trabalho.html")
```

#### 2. Gráfico de Barras: Salário Médio por Senioridade
Versão interativa do gráfico de barras de salário.

```python
senioridade_media_salario = df_limpo.groupby('senioridade')['usd'].mean().sort_values(ascending=False).reset_index()

fig_bar_plotly = px.bar(senioridade_media_salario,
                        x='senioridade',
                        y='usd',
                        title='Salário Médio por Nível de Senioridade (Interativo)',
                        labels={'usd': 'Salário Anual (USD)', 'senioridade': 'Nível de Senioridade'},
                        color='senioridade',
                        template='plotly_white')

# Para visualizar:
# fig_bar_plotly.show()
# Para salvar como HTML interativo:
fig_bar_plotly.write_html("grafico_salario_senioridade_interativo.html")
```