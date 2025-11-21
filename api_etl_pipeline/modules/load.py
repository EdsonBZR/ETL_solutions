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
        'userId': [1, 1],
        'id': [1, 3],
        'title': ['sunt aut facere repellat provident occaecati excepturi optio reprehenderit', 'ea molestias quasi exercitationem repellat qui ipsa sit aut'],
        'body': ['quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto', 'et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et deleniti harum quasi'],
        'title_length': [70, 60]
    }
    df_test_load = pd.DataFrame(data_transformed)
    print("DataFrame a ser carregado:")
    print(df_test_load)

    # O arquivo será salvo na pasta 'data' no diretório pai do módulo 'modules'
    load_data(df_test_load, '../../data/output_transformed.csv')
