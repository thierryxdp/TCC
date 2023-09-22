def conta_numero(numero,matriz):
    s=0
    for c in range(len(matriz)):
        for i in range(len(matriz[c])):
            if matriz[c][i]==x:
                s+=1
    return s