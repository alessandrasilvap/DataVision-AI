# Aqui ficará toda a lógica.
#Responsável por:
    # médias
    # estatísticas
    # valores nulos
    # tipos das colunas
def resumo_geral(tabela):
    resumo = {
        "linhas": tabela.shape[0],
        "colunas": tabela.shape[1],
        "valores_nulos": tabela.isnull().sum(),
        "total_nulos": tabela.isnull().sum().sum(),
        "duplicados": tabela.duplicated().sum(),
        "linhas_vazias": tabela.isna().all(axis=1).sum(),
        "colunas_vazias": tabela.isna().all(axis=0).sum(),
        "memoria": tabela.memory_usage(deep=True).sum(),
        "tipos": tabela.dtypes,
        "estatisticas": tabela.describe(include="all"),
    }
    
    return resumo
