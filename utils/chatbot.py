# Aqui ficará toda a lógica.
# Tudo relacionado à IA.
def responder(pergunta, dados):
    """
    Responde perguntas simples utilizando os dados da aplicação.
    """
    pergunta = pergunta.lower()

    if "linha" in pergunta:
        return f"A planilha possui {dados['linhas']} linhas."
    elif "coluna" in pergunta:
        return f"A planilha possui {dados['colunas']} colunas."
    elif "nulo" in pergunta or "vazio" in pergunta:
        return f"Foram encontrados {dados['total_nulos']} valores nulos."
    elif "duplicado" in pergunta:
        return f"Foram encontrados {dados['duplicados']} registros duplicados."
    elif "memória" in pergunta or "memoria" in pergunta:
        memoria = dados["memoria"] / 1024

        return f"A planilha utiliza aproximadamente {memoria:.2f} KB."
    else:
        return (
            "Ainda não sei responder essa pergunta. "
            "Nas próximas versões eu aprenderei novas respostas."
        )
