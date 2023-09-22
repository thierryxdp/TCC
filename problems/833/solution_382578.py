def conta_numero(numero,matriz):
    '''dado um número e uma matriz de números inteiros, conta e retorna quantas vezes aquele número aparece na matriz;
    int, list --> int'''
    soma=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if numero==matriz[i][j]:
                soma+=1
    return soma