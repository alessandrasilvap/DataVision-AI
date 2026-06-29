# Aqui ficará toda a lógica.
import pandas as pd

def carregar_planilha(arquivo):
    if arquivo.name.endswith(".csv"):
        tabela = pd.read_csv(arquivo)
    elif arquivo.name.endswith(".xlsx"):
        tabela = pd.read_excel(arquivo)
    else:
        raise ValueError("Formato de arquivo não suportado.")

    return tabela
