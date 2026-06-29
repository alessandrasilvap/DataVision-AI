# O Streamlit cria automaticamente um menu lateral com tudo que estiver dentro dessa pasta.
import streamlit as st
from utils.graficos import grafico_barras

st.title("📈 Visualização de Dados")

if "tabela" not in st.session_state:
    st.warning("Nenhuma planilha foi carregada.")
    st.stop()

tabela = st.session_state["tabela"]

tipo = st.selectbox(
    "Tipo de gráfico",
    [
        "Barras"
    ]
)

coluna = st.selectbox(
    "Escolha uma coluna",
    tabela.columns
)

if st.button("Gerar gráfico"):
    fig = grafico_barras(
        tabela,
        coluna
    )

    st.pyplot(fig)
