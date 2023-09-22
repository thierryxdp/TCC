def conta_numero (numero, matriz):
    """Retorna a quantidade de vezes em que um dado número aparece numa dada matriz.
    Entrada: int, list(list)
    Saída: int
    """
    contagem = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                contagem += 1
    return contagem