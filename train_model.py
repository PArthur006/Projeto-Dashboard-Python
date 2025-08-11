import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import OneHotEncoder
from sklearn.compose import make_column_transformer
from sklearn.pipeline import make_pipeline
import joblib

# Carrega os dados usando a mesma função do nosso app
from utils.data_loader import load_data

print("Carregando dados...")
df = load_data()

# --- Pré-processamento ---
# 1. Selecionar as features (X) e o alvo (y)
# Usaremos apenas algumas features categóricas para simplificar
features = ['senioridade', 'contrato', 'remoto', 'tamanho_empresa', 'cargo']
target = 'usd'

X = df[features]
y = df[target]

# 2. Dividir os dados em conjuntos de treino e teste
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 3. Criar um pré-processador para as colunas categóricas
# OneHotEncoder transforma categorias (ex: 'Sênior', 'Pleno') em colunas de 0s e 1s
preprocessor = make_column_transformer(
    (OneHotEncoder(handle_unknown='ignore'), features),
    remainder='passthrough'
)

# --- Treinamento do Modelo ---
# Usaremos um RandomForestRegressor, um modelo robusto e popular
model = RandomForestRegressor(n_estimators=100, random_state=42, oob_score=True)

# Criar um pipeline que primeiro pré-processa os dados e depois treina o modelo
# Isso garante que os dados de teste (e futuros dados de previsão) passem pela mesma transformação
pipeline = make_pipeline(preprocessor, model)

print("Treinando o modelo...")
pipeline.fit(X_train, y_train)

# --- Avaliação (Opcional, mas boa prática) ---
accuracy = pipeline.score(X_test, y_test)
print(f"Acurácia do modelo (R²): {accuracy:.2f}")
print(f"Pontuação Out-of-Bag (OOB): {pipeline.named_steps['randomforestregressor'].oob_score_:.2f}")

# --- Salvando o Modelo ---
# Salva o pipeline inteiro (pré-processador + modelo) em um arquivo
print("Salvando o modelo em model/salary_predictor.joblib")
joblib.dump(pipeline, 'model/salary_predictor.joblib')

print("\nTreinamento concluído e modelo salvo com sucesso!")
