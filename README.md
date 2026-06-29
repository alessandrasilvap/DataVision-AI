<img width="1355" height="597" alt="image" src="https://github.com/user-attachments/assets/5ea598a3-d8a5-46aa-b838-508df39449e5" />

# 📊 DataVision AI

Uma plataforma inteligente desenvolvida em **Python** utilizando **Streamlit** para análise de dados, visualização de informações, tratamento de dados, Machine Learning e um chatbot para auxiliar na interpretação dos resultados.

---

## 📌 Sobre o projeto

O **DataVision AI** foi desenvolvido como um projeto de estudo para consolidar conhecimentos em:

* Python
* Streamlit
* Pandas
* Visualização de Dados
* Machine Learning
* Inteligência Artificial
* Organização de projetos em módulos

A aplicação permite que o usuário envie uma planilha e obtenha automaticamente análises, gráficos, previsões e respostas para dúvidas sobre os dados.

---

# 🚀 Funcionalidades

### 📁 Upload de Planilhas

* Arquivos CSV
* Arquivos Excel (.xlsx)

---

### 📊 Análise de Dados

A aplicação realiza automaticamente:

* Quantidade de linhas
* Quantidade de colunas
* Tipos das colunas
* Valores ausentes
* Estatísticas descritivas
* Registros duplicados
* Consumo de memória
* Qualidade dos dados

---

### 📈 Visualização de Dados

O usuário pode gerar gráficos automaticamente a partir das colunas da planilha.

Atualmente o sistema possui:

* Gráfico de Barras

*(Novos gráficos poderão ser adicionados futuramente.)*

---

### 🧹 Tratamento dos Dados

O sistema permite realizar operações de limpeza da base de dados, como:

* Remover linhas com valores nulos
* Preencher valores nulos utilizando a média
* Remover registros duplicados

Após o tratamento, é exibido um resumo comparando a situação da base antes e depois da limpeza.

---

### 🤖 Modelagem Preditiva

A plataforma permite criar um modelo utilizando **Regressão Linear**.

O usuário escolhe:

* Variável alvo
* Variáveis de entrada

Após o treinamento são apresentadas métricas como:

* R²
* MAE
* RMSE

Também é possível realizar previsões utilizando o modelo treinado.

---

### 💬 Chatbot

O projeto possui um chatbot integrado capaz de responder perguntas simples sobre os dados carregados, como:

* Quantidade de linhas
* Quantidade de colunas
* Valores nulos
* Registros duplicados
* Consumo de memória

---

# 🛠 Tecnologias Utilizadas

* Python
* Streamlit
* Pandas
* NumPy
* Matplotlib
* Scikit-Learn

---

# 📂 Estrutura do Projeto

```text
DataVision AI/

│
├── pages/
│   ├── Análise.py
│   ├── Visualização.py
│   ├── Modelagem_Preditiva.py
│   ├── Chatbot.py
│   └── Tratamento_dos_Dados.py
│
├── utils/
│   ├── analise.py
│   ├── leitura.py
│   ├── graficos.py
│   ├── machine_learning.py
│   ├── chatbot.py
│   └── tratamento.py
│
├── Home.py
├── requirements.txt
└── README.md
```

---

# ▶ Como executar

### Clone o repositório

```bash
git clone https://github.com/SEU-USUARIO/DataVision-AI.git
```

---

### Entre na pasta

```bash
cd DataVision-AI
```

---

### Instale as dependências

```bash
pip install -r requirements.txt
```

---

### Execute a aplicação

```bash
streamlit run Home.py
```

---

# 🎯 Objetivos do Projeto

Este projeto foi desenvolvido para praticar:

* Manipulação de dados com Pandas;
* Desenvolvimento de aplicações web com Streamlit;
* Criação de gráficos;
* Tratamento de dados;
* Machine Learning com Scikit-Learn;
* Organização de projetos em Python;
* Integração entre diferentes módulos da aplicação.

---

# 🚀 Melhorias Futuras

Algumas funcionalidades planejadas para versões futuras:

* Novos tipos de gráficos;
* Mais algoritmos de Machine Learning;
* Exportação de relatórios em PDF;
* Integração com APIs de Inteligência Artificial (OpenAI, Gemini, Ollama);
* Chatbot capaz de responder perguntas diretamente sobre a planilha enviada.

---

# 👩‍💻 Desenvolvido por

**Alessandra Cristina**

Projeto desenvolvido para fins de estudo e aprimoramento em Ciência de Dados, Machine Learning e Desenvolvimento Web com Python.
