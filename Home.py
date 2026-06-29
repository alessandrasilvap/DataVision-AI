# Será a página principal.
import streamlit as st
from utils.analise import resumo_geral
from utils.leitura import carregar_planilha

# Configurações da página.
st.set_page_config(
    page_title="DataVision AI",
    page_icon= "📊",
    layout="wide"
)

# Título 
st.title("📊 DataVision AI")

# Descrição
st.write("""
Bem-vindo à plataforma inteligente para análise de dados.
         
Nesta aplicação, você poderá:
         
- 📁 Enviar planilhas CSV ou Excel;
- 📊 Gerar análises automáticas;
- 📈 Visualizar gráficos;
- 🤖 Criar previsões utilizando Machine Learning;
- 💬 Conversar com um chatbot para entender seus dados.
""")

st.divider()

#Upload
arquivo = st.file_uploader(
    "Selecione uma planilha",
    type=["csv", "xlsx"]
)

st.divider()

# Área reservada
st.subheader("📄 Informações da planilha")

if arquivo is None:
    st.info("Nenhuma planilha foi enviada.")
else:
    tabela = carregar_planilha(arquivo)
    st.session_state["tabela"] = tabela
    dados = resumo_geral(tabela)
    st.session_state["dados"] = dados

    st.success("Planilha carregada com sucesso!")

    st.subheader("Pré-visualização")
    st.dataframe(tabela)

    st.divider()

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric("Linhas", dados["linhas"])
    with col2:
        st.metric("Colunas", dados["colunas"])
    with col3:
        st.metric("Valores vazios", dados["total_nulos"])
    with col4:
        st.metric("Duplicados", dados["duplicados"])
