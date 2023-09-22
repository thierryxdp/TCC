def conta_numero(numero,matriz):
    i=0
    j=0
    while i<len(matriz):
        j=matriz[i].count(numero)+j
        i=i+1
    return j