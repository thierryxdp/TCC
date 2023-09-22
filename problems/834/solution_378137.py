def media_matriz(matriz: list)-> float:
    """Função que dada uma matriz, retorna a média de todos os números desta matriz."""

    soma_numeros = 0
    qtd_numeros = 0

    for numeros in matriz:
        soma_numeros += sum(numeros)
        qtd_numeros += len(numeros)

    return round((soma_numeros/qtd_numeros),2)