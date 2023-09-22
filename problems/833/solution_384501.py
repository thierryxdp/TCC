def conta_numero(numero,matriz):
    i=0
    j=0
    if len(matriz)==0:
        return 0
    while i<len(matriz):
        if matriz[j][i]==numero:
            j=j+1
            i=i+1
        else:
            i=i+1
    return j+1