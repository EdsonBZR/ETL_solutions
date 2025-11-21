import requests
import pandas as pd
from typing import List, Dict, Any

def extract_from_api(url: str, params: Dict[str, Any] = None) -> List[Dict[str, Any]]:
    """
    Extrai dados de uma API RESTful.

    Args:
        url (str): A URL do endpoint da API.
        params (Dict[str, Any], optional): Parâmetros para a requisição GET. Defaults to None.

    Returns:
        List[Dict[str, Any]]: Uma lista de dicionários (objetos JSON) com os dados extraídos.
    """
    print(f"Iniciando extração da API: {url}")
    try:
        response = requests.get(url, params=params)
        response.raise_for_status()  # Levanta um erro para códigos de status HTTP 4xx/5xx

        data = response.json()
        print(f"Dados extraídos com sucesso da API. {len(data)} registros recebidos.")
        return data
    except requests.exceptions.HTTPError as http_err:
        print(f"Erro HTTP ao extrair dados da API: {http_err}")
    except requests.exceptions.ConnectionError as conn_err:
        print(f"Erro de conexão ao extrair dados da API: {conn_err}")
    except requests.exceptions.Timeout as timeout_err:
        print(f"Timeout ao extrair dados da API: {timeout_err}")
    except requests.exceptions.RequestException as req_err:
        print(f"Erro geral na requisição ao extrair dados da API: {req_err}")
    except ValueError:
        print(f"Erro: Resposta da API não é um JSON válido.")
    return []

if __name__ == '__main__':
    # Exemplo de uso
    API_URL = "https://jsonplaceholder.typicode.com/posts"
    posts_data = extract_from_api(API_URL)
    if posts_data:
        print("\nPrévia dos dados extraídos (primeiros 2 posts):")
        # Converte para DataFrame para visualização mais fácil
        df_posts = pd.DataFrame(posts_data)
        print(df_posts.head(2))
