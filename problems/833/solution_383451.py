def conta_numero(numero, matriz):
    '''Função que tendo como entrada um numero inteiro e uma matriz
    retorna quantas vezes aquele numero aparece na matriz
    int, list -> int'''
    qtd= 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == numero:
                qtd= qtd + 1
    return qtd