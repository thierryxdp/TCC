def conta_numero(numero,matriz):
    """funcao que conta quantas vezes o numero passado na entrada aparece na matriz.
    int,list-->int"""
    cont=0
    if matriz==[]:
        return 0
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j]==numero:
                cont+=1
     return cont