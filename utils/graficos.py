# Aqui ficará toda a lógica.
# Todos os gráficos.
import matplotlib.pyplot as plt

def grafico_barras(tabela, coluna):
    fig, ax = plt.subplots(figsize=(8,5))

    tabela[coluna].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title(f"Distribuição - {coluna}")
    ax.set_xlabel(coluna)
    ax.set_ylabel("Quantidade")

    plt.xticks(rotation=45)

    return fig
