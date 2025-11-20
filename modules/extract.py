import pandas as pd

def extract_data(filepath: str) -> pd.DataFrame:
    """
    Extrai dados de um arquivo CSV.

    Args:
        filepath (str): O caminho para o arquivo CSV de entrada.

    Returns:
        pd.DataFrame: Um DataFrame pandas contendo os dados extraídos.
    """
    try:
        df = pd.read_csv(filepath)
        print(f"Dados extraídos com sucesso de: {filepath}")
        return df
    except FileNotFoundError:
        print(f"Erro: O arquivo não foi encontrado em {filepath}")
        return pd.DataFrame()
    except Exception as e:
        print(f"Erro durante a extração de dados: {e}")
        return pd.DataFrame()

if __name__ == '__main__':
    # Exemplo de uso
    # Certifique-se de que o input.csv está na pasta data/
    df_extracted = extract_data('../../data/input.csv')
    if not df_extracted.empty:
        print("\nPrévia dos dados extraídos:")
        print(df_extracted.head())
