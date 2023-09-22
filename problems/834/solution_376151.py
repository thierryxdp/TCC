def media_matriz(matriz):
    """Funcao recebe uma matriz dada: matriz nao vazia e retorna a media
    de todos os numeros dela """

    qtd_numeros = 0
    soma_numeros = 0

    for linha in range(len(matriz)):
        for coluna in range(len(matriz[linha])):
            qtd_numeros += 1
            soma_numeros += matriz[linha][coluna]

    media = round(soma_numeros/qtd_numeros, 2)

    return media