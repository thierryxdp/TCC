def conta_numero(numero, matriz):
    n=0
    for k in matriz[n]:
        k=0
        for c in matriz[n]:
            if c == numero:
                k=k+1
    return k