# O Streamlit cria automaticamente um menu lateral com tudo que estiver dentro dessa pasta.
import streamlit as st
import pandas as pd
from utils.machine_learning import (
    obter_colunas_numericas,
    validar_base,
    preparar_dados,
    treinar_regressao_linear,
    avaliar_modelo,
    realizar_previsao
)

st.title("🤖 Modelagem Preditiva")

st.divider()

if "tabela" not in st.session_state:
    st.warning("Nenhuma planilha foi carregada.")
    st.stop()

tabela = st.session_state["tabela"]

colunas = obter_colunas_numericas(tabela)

if not validar_base(colunas):
    st.error(
        "A planilha precisa possuir pelo menos duas colunas numéricas para utilizar Machine Learning."
    )
    st.stop()

variavel_alvo = st.selectbox(
    "Escolha a variável que deseja prever",
    colunas
)

variaveis = st.multiselect(
    "Escolha as variáveis utilizadas para a previsão",
    colunas,
    default=[
        c for c in colunas
        if c != variavel_alvo
    ]
)

if st.button("Treinar Modelo"):
    if len(variaveis) == 0:
        st.error("Selecione pelo menos uma variável.")
        st.stop()

    X, y = preparar_dados(
        tabela,
        variaveis,
        variavel_alvo
    )

    modelo, y_teste, previsoes = treinar_regressao_linear(
        X,
        y
    )

    st.session_state["modelo"] = modelo
    st.session_state["variaveis"] = variaveis
    st.session_state["variavel_alvo"] = variavel_alvo

    metricas = avaliar_modelo(
        y_teste,
        previsoes
    )

    st.success("Modelo treinado com sucesso!")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("R²", f"{metricas['R²']:.3f}")

    with col2:
        st.metric("MAE", f"{metricas['MAE']:.3f}")

    with col3:
        st.metric("RMSE", f"{metricas['RMSE']:.3f}")

# Área de previsão
if "modelo" in st.session_state:
    st.divider()

    st.subheader("🔮 Fazer uma previsão")

    dados_usuario = {}

    for coluna in st.session_state["variaveis"]:
        valor = st.number_input(
            f"{coluna}",
            value=0.0
        )

        dados_usuario[coluna] = valor

    if st.button("Prever"):
        entrada = pd.DataFrame([dados_usuario])

        resultado = realizar_previsao(
            st.session_state["modelo"],
            entrada
        )

        st.success("Previsão realizada com sucesso!")

        st.metric(
            f"{st.session_state['variavel_alvo']} previsto(a)",
            f"{resultado[0]:.2f}"
        )
