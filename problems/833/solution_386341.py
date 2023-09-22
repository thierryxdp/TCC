def conta_numero(numero,matriz):
    ''' '''
    x=0
    if matriz==[]:
        return 0
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j==numero:
                x+=1
    return x