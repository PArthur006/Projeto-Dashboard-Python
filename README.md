# 📊 Dashboard de Análise de Salários em Dados

Dashboard interativo para análise de salários em tecnologia e dados, usando Python e Streamlit. Iniciado na Imersão de Dados da Alura, foi aprimorado para um portfólio completo.

---

## 🚀 Sobre o Projeto

O dashboard oferece uma ferramenta visual para explorar tendências salariais na área de dados. Usuários podem filtrar por ano, experiência, contrato e tamanho da empresa.

### ✨ Funcionalidades

- **Dashboard Interativo:** Interface com Streamlit.
- **Filtros Dinâmicos:** Múltiplos filtros para refinar a análise.
- **KPIs:** Métricas de salário médio, máximo e total de registros.
- **Visualizações:**
  - Top 10 cargos com maiores salários.
  - Histograma de distribuição salarial.
  - Gráfico de trabalho remoto, híbrido e presencial.
  - Mapa com média salarial de Cientistas de Dados por país.
- **Tabela de Dados:** Explore os dados brutos na interface.

---

## 🛠️ Tecnologias

- **Python:** Linguagem principal.
- **Pandas:** Manipulação de dados.
- **Streamlit:** Criação do dashboard.
- **Plotly:** Gráficos interativos.

---

## ⚙️ Como Executar

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/PArthur006/alura-python_dados.git
    cd alura-python_dados
    ```

2.  **Crie e ative um ambiente virtual:**
    ```bash
    # Linux/macOS
    python3 -m venv .venv && source .venv/bin/activate

    # Windows
    python -m venv .venv && .venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

O dashboard abrirá no seu navegador.

---

## 📄 Fonte dos Dados

Os dados são da Imersão de Dados da Alura, disponíveis [aqui](https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv), com informações de 2020 a 2024.
