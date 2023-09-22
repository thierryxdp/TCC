def conta_numero(numero,matriz):
    '''
    Funçao que dado um numero inteiro e uma matriz de inteiros de tamanho qualquer,
    conta e retorna quantas vezes aquele numero aparece na matriz
    int,list(list) -> int
    '''
    qtd = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                qtd = qtd + 1
    return qtd