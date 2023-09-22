def conta_numero(numero,matriz):
    '''função que verifica quantas vezes um numero se repete na matriz
    int,list--->int'''
    if matriz == []:
        return 0
    vezes =0
    for i in range(len(matriz)):
        for j in range (len(matriz[0])):
            if numero == matriz[i][j]:
                vezes+=1
    return vezes