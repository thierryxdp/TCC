def conta_numero(numero,matriz):
    """ """
    l=[]
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            l=l+[matriz[i][j]]
    return l.count(numero)