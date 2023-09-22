def conta_numero (numero, matriz):
    '''Dado um número inteiro e uma matriz, conta e retorne 
       quantas vezes aquele número aparece na matriz;
       int, lis -> int'''
    aparece = 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if numero==matriz[i][j]:
                aparece = aparece+1
    return aparece