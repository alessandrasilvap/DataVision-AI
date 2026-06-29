# O Streamlit cria automaticamente um menu lateral com tudo que estiver dentro dessa pasta.
import streamlit as st
from utils.chatbot import responder

st.title("💬 Chatbot IA")

if "dados" not in st.session_state:
    st.warning("Nenhuma planilha foi carregada.")
    st.stop()

dados = st.session_state["dados"]

pergunta = st.text_input(
    "Digite sua pergunta"
)

if st.button("Perguntar"):
    resposta = responder(
        pergunta,
        dados
    )
