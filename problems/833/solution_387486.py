def conta_numero(numero,matriz):
    '''dada uma matriz, retorna quantas vezes o numero dado
    aparece naquela matriz
    int,list-> int
    '''
    quantidade=0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j]==numero:
                quantidade+=1
    return quantidade