def conta_numero(numero, matriz):
    n=0
    for i in matriz[n]:
        k=0
        for c in matriz[n]:
            n=n+1
            if c == numero:
                k=k+1
    return k