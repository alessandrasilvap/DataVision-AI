def remover_nulos(tabela):
    """
    Remove todas as linhas que possuem valores nulos.
    """
    return tabela.dropna()


def remover_duplicados(tabela):
    """
    Remove registros duplicados.
    """
    return tabela.drop_duplicates()


def preencher_media(tabela):
    """
    Preenche valores nulos das colunas numéricas com a média.
    """
    tabela = tabela.copy()

    colunas = tabela.select_dtypes(include=["number"]).columns

    for coluna in colunas:
        tabela[coluna] = tabela[coluna].fillna(
            tabela[coluna].mean()
        )

    return tabela
