import streamlit as st
import joblib
import pandas as pd
import os
import gdown

def download_model_from_gdrive(gdrive_id, output_path):
    """
    Baixa um arquivo do Google Drive usando o gdown.
    """
    try:
        print(f"Baixando o modelo do Google Drive... ID: {gdrive_id}")
        gdown.download(id=gdrive_id, output=output_path, quiet=False)
        print(f"Modelo baixado com sucesso em: {output_path}")
        return True
    except Exception as e:
        st.error(f"Falha ao baixar o modelo do Google Drive: {e}")
        print(f"Falha ao baixar o modelo: {e}")
        return False

@st.cache_resource
def load_model():
    """
    Carrega o pipeline de modelo treinado. Se não existir localmente,
    baixa do Google Drive. Usa @st.cache_resource para otimização.
    """
    script_dir = os.path.dirname(__file__)
    model_dir = os.path.join(script_dir, '..', 'model')
    model_path = os.path.join(model_dir, 'salary_predictor.joblib')
    
    # Garante que o diretório do modelo exista
    os.makedirs(model_dir, exist_ok=True)

    # Verifica se o modelo já existe localmente
    if not os.path.exists(model_path):
        st.info("Modelo não encontrado localmente. Baixando do Google Drive...")
        # ID do arquivo no Google Drive
        gdrive_id = "1MaaqxFSwZ0nmW_bx65RRxF94IpraCj3v"
        download_success = download_model_from_gdrive(gdrive_id, model_path)
        if not download_success:
            return None # Falha no download

    # Carrega o modelo do arquivo local
    try:
        print(f"Tentando carregar o modelo de: {os.path.abspath(model_path)}")
        pipeline = joblib.load(model_path)
        print("Modelo carregado com sucesso!")
        st.success("Modelo de previsão carregado com sucesso!")
        return pipeline
    except FileNotFoundError:
        st.error("Arquivo do modelo não encontrado após tentativa de download.")
        print("Erro: Arquivo do modelo não encontrado.")
        return None
    except Exception as e:
        st.error(f"Ocorreu um erro inesperado ao carregar o modelo: {e}")
        print(f"Ocorreu um erro inesperado ao carregar o modelo: {e}")
        return None

def make_prediction(pipeline, user_input):
    """
    Recebe o pipeline e os dados do usuário e retorna a previsão salarial.
    """
    try:
        input_df = pd.DataFrame([user_input])
        prediction = pipeline.predict(input_df)
        return prediction[0]
    except Exception as e:
        st.error(f"Erro ao realizar a previsão: {e}")
        return None