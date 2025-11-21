import pandas as pd
from typing import List, Dict, Any

def transform_data(data: List[Dict[str, Any]]) -> pd.DataFrame:
    """
    Transforma os dados:
    1. Converte a lista de dicionários em um DataFrame.
    2. Cria uma nova coluna 'title_length' com o comprimento do título.
    3. Filtra posts com 'title_length' maior que 20 caracteres.

    Args:
        data (List[Dict[str, Any]]): Uma lista de dicionários com os dados extraídos.

    Returns:
        pd.DataFrame: O DataFrame com as transformações aplicadas.
    """
    if not data:
        print("Erro: A lista de dados de entrada para transformação está vazia.")
        return pd.DataFrame()

    print("Iniciando transformação de dados...")

    # 1. Converte para DataFrame
    df = pd.DataFrame(data)
    print(f"DataFrame criado com {len(df)} registros.")

    # 2. Cria uma nova coluna 'title_length'
    df['title_length'] = df['title'].apply(len)
    print("Coluna 'title_length' adicionada.")

    # 3. Filtra posts com title_length > 20
    df_filtered = df[df['title_length'] > 20].copy()
    print(f"Dados filtrados: {len(df_filtered)} registros restantes (title_length > 20).")

    print("Transformação de dados concluída.")
    return df_filtered

if __name__ == '__main__':
    # Exemplo de uso (simulando dados extraídos da API)
    sample_data = [
        {"userId": 1, "id": 1, "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit", "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"},
        {"userId": 1, "id": 2, "title": "qui est esse", "body": "est rerum tempore vitae\nsequi sint nihil reprehenderit dolor beatae ea dolores neque\nfugiat blanditiis voluptate porro vel nihil molestiae ut reiciendis\nqui aperiam non debitis possimus qui neque nisi nulla"},
        {"userId": 1, "id": 3, "title": "ea molestias quasi exercitationem repellat qui ipsa sit aut", "body": "et iusto sed quo iure\nvoluptatem occaecati omnis eligendi aut ad\nvoluptatem doloribus vel accusantium quis pariatur\nmolestiae porro eius odio et labore et deleniti harum quasi"},
    ]
    df_transformed = transform_data(sample_data)
    if not df_transformed.empty:
        print("\nPrévia dos dados transformados:")
        print(df_transformed.head())
