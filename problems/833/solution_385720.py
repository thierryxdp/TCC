def conta_numero(numero,matriz):
    """ """
    l=[]
    for i in len(matriz):
        for j in len(matriz[0]):
            l=l+[matriz[i][j]]
    return l.count(numero)