def conta_numero(n,matriz):
    '''dado um número inteiro (n) e uma matriz de inteiros de qualquer tamanho (mat), conta e retorna a quantidade de vezes que aquele número (n) aparece na matrzi (mat); int,mat -> int'''

    cont = 0
    
    for i in range(0,len(matriz)):
        for j in range(0,len(matriz[i])):
            if matriz[i][j] == n:
                cont = cont + 1
    return cont