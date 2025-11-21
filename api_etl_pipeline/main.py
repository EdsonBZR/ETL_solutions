import os
from modules.extract_api import extract_from_api
from modules.transform import transform_data
from modules.load import load_data
import pandas as pd # Necessário para o main.py no teste do extract

def run_etl_pipeline():
    """
    Executa o pipeline ETL completo.
    Extrai dados de uma API, transforma-os e os carrega em um CSV.
    """
    print("Iniciando o pipeline ETL (Extração da API)...")

    # Definir URL da API e caminho do arquivo de saída
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    current_dir = os.path.dirname(__file__)
    output_filepath = os.path.join(current_dir, '..', 'api_resultados', 'output_transformed.csv')

    # 1. Etapa de Extração
    print("\n--- ETAPA DE EXTRAÇÃO (API) ---")
    extracted_data = extract_from_api(API_URL)
    if not extracted_data:
        print("Pipeline interrompido devido a falha na extração ou dados vazios.")
        return

    # 2. Etapa de Transformação
    print("\n--- ETAPA DE TRANSFORMAÇÃO ---")
    df_transformed = transform_data(extracted_data)
    if df_transformed.empty:
        print("Pipeline interrompido devido a falha na transformação ou dados vazios.")
        return

    # 3. Etapa de Carregamento
    print("\n--- ETAPA DE CARREGAMENTO ---")
    load_data(df_transformed, output_filepath)

    print("\nPipeline ETL (API) concluído com sucesso!")

if __name__ == '__main__':
    run_etl_pipeline()
