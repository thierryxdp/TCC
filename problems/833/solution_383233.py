def conta_numero(numero, matriz):
    '''funcao que dados um numero inteiro e uma matriz de inteiros, conta e retorna quantas vezes o numero aparece na matriz
       int, matriz(int) -> int'''
    contador = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador += 1
    return contador