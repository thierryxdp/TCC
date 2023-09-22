def conta_numero(numero,matriz):
    i=0
    j=0
    while i<len(matriz):
        if matriz[i][j]==numero:
            j=j+1
            i=i+1
        elif j=0:
            j=j-1
        else:
            i=i+1
    return j+1