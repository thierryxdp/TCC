def conta_numero(numero,matriz):
    s=0
    for c in range(len(matriz)):
        if matriz[c]==numero:
            s+=1
        for i in range(c):
            if matriz[c][i]==numero:
                s+=1
    return s