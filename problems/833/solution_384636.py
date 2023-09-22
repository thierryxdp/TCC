def conta_numero(numero, matriz):
    '''função que, dado um número(numero) inteiro e uma matriz(matriz), conta quantas vezes
    o número informado aparece na matriz. int,list->int'''
    contador=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] == numero:
                contador=contador+1
    return contador