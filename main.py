import os
from modules.extract import extract_data
from modules.transform import transform_data
from modules.load import load_data

def run_etl_pipeline():
    """
    Executa o pipeline ETL completo.
    """
    print("Iniciando o pipeline ETL...")

    # Definir caminhos dos arquivos
    current_dir = os.path.dirname(__file__)
    input_filepath = os.path.join(current_dir, 'data', 'input.csv')
    output_filepath = os.path.join(current_dir, 'data', 'output_transformed.csv')

    # 1. Etapa de Extração
    print("\n--- ETAPA DE EXTRAÇÃO ---")
    df_extracted = extract_data(input_filepath)
    if df_extracted.empty:
        print("Pipeline interrompido devido a falha na extração.")
        return

    # 2. Etapa de Transformação
    print("\n--- ETAPA DE TRANSFORMAÇÃO ---")
    df_transformed = transform_data(df_extracted)
    if df_transformed.empty:
        print("Pipeline interrompido devido a falha na transformação.")
        return

    # 3. Etapa de Carregamento
    print("\n--- ETAPA DE CARREGAMENTO ---")
    load_data(df_transformed, output_filepath)

    print("\nPipeline ETL concluído com sucesso!")

if __name__ == '__main__':
    run_etl_pipeline()
