import pandas as pd

def transform_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Transforma os dados:
    1. Filtra registros onde a idade é maior que 25.
    2. Cria uma nova coluna 'status_salario' baseada no salário.

    Args:
        df (pd.DataFrame): O DataFrame a ser transformado.

    Returns:
        pd.DataFrame: O DataFrame com as transformações aplicadas.
    """
    if df.empty:
        print("Erro: DataFrame de entrada para transformação está vazio.")
        return pd.DataFrame()

    print("Iniciando transformação de dados...")

    # 1. Filtrar registros onde a idade é maior que 25
    df_filtered = df[df['idade'] > 25].copy()
    print(f"Dados filtrados: {len(df_filtered)} registros restantes (idade > 25).")

    # 2. Criar uma nova coluna 'status_salario'
    df_filtered['status_salario'] = df_filtered['salario'].apply(
        lambda x: 'Alto' if x >= 5000 else 'Médio' if x >= 3000 else 'Baixo'
    )
    print("Coluna 'status_salario' adicionada.")

    print("Transformação de dados concluída.")
    return df_filtered

if __name__ == '__main__':
    # Exemplo de uso (simulando um DataFrame extraído)
    data = {
        'id': [1, 2, 3, 4, 5, 6],
        'nome': ['Alice', 'Bob', 'Carlos', 'Diana', 'Eduardo', 'Fernanda'],
        'idade': [30, 24, 35, 29, 22, 40],
        'cidade': ['Sao Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Sao Paulo', 'Curitiba', 'Rio de Janeiro'],
        'salario': [5000, 3500, 6000, 4800, 3000, 7000]
    }
    df_test = pd.DataFrame(data)
    print("DataFrame original para teste:")
    print(df_test)

    df_transformed = transform_data(df_test)
    if not df_transformed.empty:
        print("\nPrévia dos dados transformados:")
        print(df_transformed.head())
