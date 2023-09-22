def repetidos(lista):
    """Retorna o número de repetições consecutivas numa dada lista.
    Entrada: lista
    Saída: int
    """
    contagem = 1
    resultado = 0
    while contagem < len(lista):
        if lista[contagem] = lista[contagem-1]:
            resultado += 1
        contagem += 1
    return resultado