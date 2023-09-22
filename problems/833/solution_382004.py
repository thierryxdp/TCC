def conta_numero(numero, matriz):
    """Funcao conta e retorna quantas vezes um numero dado: numero aparece
    na matriz dada: matriz """

    contador = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            if numero == matriz[linha][coluna]:
                contador += 1

    return contador