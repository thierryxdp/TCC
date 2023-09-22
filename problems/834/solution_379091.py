def media_matriz(matriz):
    '''
    Função que retorna a média de todos os números de uma matriz.
    list -> float
    '''
    soma_matriz = 0
    peso_matriz = len(matriz) * len(matriz[0])
    linhas = len(matriz)
    colunas = len(matriz[0])
    for elem in range(linhas):
        for elem2 in range(colunas):
            soma_matriz = soma_matriz + matriz[elem][elem2]
    return round((soma_matriz /peso_matriz),2)