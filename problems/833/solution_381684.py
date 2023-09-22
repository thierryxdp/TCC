def conta_numero(n, matriz):
    '''dado um número inteiro e uma matriz de inteiros, retorna quantas 
    vezes aquele número aparece na matriz.
    int, list ->int'''
    conta =0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] ==n:
                conta +=1
    return conta