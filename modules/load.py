import pandas as pd
import os

def load_data(df: pd.DataFrame, output_filepath: str):
    """
    Carrega os dados em um arquivo CSV.

    Args:
        df (pd.DataFrame): O DataFrame a ser carregado.
        output_filepath (str): O caminho para o arquivo CSV de saída.
    """
    if df.empty:
        print("Erro: DataFrame de entrada para carregamento está vazio. Nada para salvar.")
        return

    try:
        # Garante que o diretório de saída exista
        output_dir = os.path.dirname(output_filepath)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
            print(f"Diretório '{output_dir}' criado.")

        df.to_csv(output_filepath, index=False)
        print(f"Dados carregados com sucesso em: {output_filepath}")
    except Exception as e:
        print(f"Erro durante o carregamento de dados: {e}")

if __name__ == '__main__':
    # Exemplo de uso (simulando um DataFrame transformado)
    data_transformed = {
        'id': [1, 3, 4, 6],
        'nome': ['Alice', 'Carlos', 'Diana', 'Fernanda'],
        'idade': [30, 35, 29, 40],
        'cidade': ['Sao Paulo', 'Belo Horizonte', 'Sao Paulo', 'Rio de Janeiro'],
        'salario': [5000, 6000, 4800, 7000],
        'status_salario': ['Alto', 'Alto', 'Médio', 'Alto']
    }
    df_test_load = pd.DataFrame(data_transformed)
    print("DataFrame a ser carregado:")
    print(df_test_load)

    # O arquivo será salvo na pasta 'data' no diretório pai do módulo 'modules'
    load_data(df_test_load, '../../data/output_transformed.csv')
