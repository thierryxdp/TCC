def media_matriz(matriz):
    '''função que recebe uma matriz e retorna a media desta matriz. list -> int'''
    soma_matriz = 0
    num_elementos =0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            soma_matriz +=matriz[i][j]
            num_elementos += 1
    return round(soma_matriz/num_elementos,2)