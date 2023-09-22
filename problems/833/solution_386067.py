def conta_numero(numero,matriz):
    '''Retorna a quantidade de vezes que numero aparece em matriz.
    int,list(list)->int'''
    cont=0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                cont+=1
    return cont