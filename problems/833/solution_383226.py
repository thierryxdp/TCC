def conta_numero(num,matriz):
    """Dado um número inteiro e uma matriz de números inteiros, respectivamente, a função no diz quantas vezes o número aparece na matriz; int, list -> int"""
    
    contador = 0
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == num:
                contador = contador + 1
    return contador