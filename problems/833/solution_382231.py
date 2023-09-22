def conta_numero(numero, matriz):
    n=0
    for k in matriz[n]:
        n=n+1
        if k == numero:
            k=k+1
    return k