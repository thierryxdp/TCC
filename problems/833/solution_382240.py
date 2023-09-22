def conta_numero(numero, matriz):
    n=0
    for i in matriz[n]:
        n=n+1
        k=0
        for c in matriz[n]:
            if c == numero:
                k=k+1
    return k