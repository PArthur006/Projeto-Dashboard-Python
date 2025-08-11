# 📊 Dashboard de Análise de Salários em Dados

Dashboard interativo para análise de salários em tecnologia e dados, usando Python e Streamlit. Iniciado na Imersão de Dados da Alura, foi aprimorado para um portfólio completo.

![Exemplo do Dashboard](https://i.imgur.com/YOUR_SCREENSHOT_URL.png) 
*(Dica: Substitua o link acima por um print da sua aplicação para exibir uma imagem do projeto!)*

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
- **Previsão Salarial:** Estime salários com base em experiência, contrato, trabalho, empresa e cargo.

---

## 🛠️ Tecnologias

- **Python:** Linguagem principal.
- **Pandas:** Manipulação de dados.
- **Streamlit:** Criação do dashboard.
- **Plotly:** Gráficos interativos.
- **Scikit-learn:** Modelo de Machine Learning.

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

4.  **Treine o modelo:**
    ```bash
    python train_model.py
    ```
    *(Este comando treina o modelo de Machine Learning e o salva localmente. O arquivo do modelo não é versionado no Git, seguindo as boas práticas.)*

5.  **Execute a aplicação:**
    ```bash
    streamlit run app.py
    ```

O dashboard abrirá no seu navegador.

---

## 🤖 Modelo de Machine Learning

O projeto usa um modelo de regressão com `scikit-learn` para prever salários. O script `train_model.py` treina e salva o modelo em `model/`.

O modelo usa um `Pipeline` com `OneHotEncoder` e `RandomForestRegressor`.

**Nota sobre Versionamento:** O arquivo do modelo treinado (`salary_predictor.joblib`) não é e não deve ser salvo no repositório Git. A pasta `model/` está incluída no `.gitignore`. Isso é uma prática recomendada para:

- **Manter o repositório leve:** Arquivos de modelo podem ser grandes e ineficientes para o Git.
- **Garantir a reprodutibilidade:** O modelo pode ser recriado a qualquer momento usando o script de treino e os dados, o que é mais confiável do que salvar o arquivo binário.
- **Evitar problemas de compatibilidade:** Arquivos de modelo podem não ser compatíveis entre diferentes versões de bibliotecas ou arquiteturas de sistema.

---

## 📄 Fonte dos Dados

Os dados são da Imersão de Dados da Alura, disponíveis [aqui](https://raw.githubusercontent.com/guilhermeonrails/data-jobs/refs/heads/main/salaries.csv), com informações de 2020 a 2024.
