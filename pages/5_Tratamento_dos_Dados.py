# O Streamlit cria automaticamente um menu lateral com tudo que estiver dentro dessa pasta.
import streamlit as st
from utils.analise import resumo_geral  
from utils.tratamento import (
    preencher_media, 
    remover_duplicados, 
    remover_nulos
)

st.title("🧹 Tratamento dos Dados")

if "tabela" not in st.session_state:
    st.warning("Nenhuma planilha foi carregada.")
    st.stop()

tabela = st.session_state["tabela"]

st.subheader("Pré-visualização")

st.dataframe(tabela.head())

opcao = st.radio(
    "Escolha um tratamento",
    [
        "Remover linhas com valores nulos",
        "Preencher valores nulos com a média",
        "Remover registros duplicados"
    ]
)

linhas_antes = len(tabela)
nulos_antes = tabela.isnull().sum().sum()
duplicados_antes = tabela.duplicated().sum()

if st.button("Aplicar Tratamento"):
    if opcao == "Remover linhas com valores nulos":
        tabela = remover_nulos(tabela)

    elif opcao == "Preencher valores nulos com a média":
        tabela = preencher_media(tabela)

    elif opcao == "Remover registros duplicados":
        tabela = remover_duplicados(tabela)

    st.session_state["tabela"] = tabela
    st.session_state["dados"] = resumo_geral(tabela)
    # Informações depois do tratamento
    linhas_depois = len(tabela)
    nulos_depois = tabela.isnull().sum().sum()
    duplicados_depois = tabela.duplicated().sum()

    st.success("Tratamento aplicado com sucesso!")

    st.subheader("Resumo do Tratamento")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Linhas",
            linhas_depois,
            delta=linhas_depois - linhas_antes
        )

    with col2:
        st.metric(
            "Valores Nulos",
            nulos_depois,
            delta=nulos_depois - nulos_antes
        )

    with col3:
        st.metric(
            "Duplicados",
            duplicados_depois,
            delta=duplicados_depois - duplicados_antes
        )

    st.dataframe(tabela.head())
