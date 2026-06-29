# Aqui ficará toda a lógica.
# Responsável por:
    # Treinamento.
    # Predição.
    # Avaliação.
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error
import math

def obter_colunas_numericas(tabela):
    """
    Retorna apenas as colunas numéricas da tabela.
    """
    return tabela.select_dtypes(include=["number"]).columns.tolist()

def validar_base(colunas):
    """
    Verifica se há colunas suficientes para Machine Learning.
    """
    return len(colunas) >= 2

def preparar_dados(tabela, variaveis, variavel_alvo):
    """
    Separa as variáveis de entrada (X) e a variável alvo (y).
    """
    X = tabela[variaveis].copy()
    y = tabela[variavel_alvo].copy()

    # Junta tudo
    dados = pd.concat([X, y], axis=1)

    # Remove linhas com valores vazios
    dados = dados.dropna()

    # Separa novamente
    X = dados[variaveis]
    y = dados[variavel_alvo]

    return X, y

def treinar_regressao_linear(X, y):
    """
    Treina um modelo de Regressão Linear.
    """
    X_treino, X_teste, y_treino, y_teste = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    modelo = LinearRegression()

    modelo.fit(X_treino, y_treino)

    previsoes = modelo.predict(X_teste)

    return modelo, y_teste, previsoes

def avaliar_modelo(y_teste, previsoes):
    """
    Calcula as métricas do modelo.
    """
    r2 = r2_score(y_teste, previsoes)

    mae = mean_absolute_error(y_teste, previsoes)

    rmse = math.sqrt(
        mean_squared_error(y_teste, previsoes)
    )

    return {
        "R²": r2,
        "MAE": mae,
        "RMSE": rmse
    }

def realizar_previsao(modelo, dados_entrada):
    """
    Realiza uma previsão utilizando o modelo treinado.
    """
    previsao = modelo.predict(dados_entrada)

    return previsao
