# O Streamlit cria automaticamente um menu lateral com tudo que estiver dentro dessa pasta.
import streamlit as st

st.title("📊 Análise de Dados")

if "tabela" not in st.session_state:
    st.warning("Nenhuma planilha foi carregada.")
    st.stop()

dados = st.session_state["dados"]

st.subheader("📌 Tipos das Colunas")
st.dataframe(dados["tipos"])

st.divider()

st.subheader("⚠ Valores Ausentes")
st.dataframe(dados["valores_nulos"])

st.divider()

st.subheader("📈 Estatísticas")
st.dataframe(dados["estatisticas"])

st.divider()

st.subheader("🧹 Qualidade dos Dados")

col1, col2 = st.columns(2)

with col1:
    st.metric("Linhas Vazias", dados["linhas_vazias"])
    st.metric("Duplicados", dados["duplicados"])

with col2:
    st.metric("Colunas Vazias", dados["colunas_vazias"])
    st.metric("Memória (KB)", f"{dados['memoria']/1024:.2f}")
