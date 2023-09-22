def conta_numero(n,P):
    contador=0
    for i in P:
        for j in i:
            if n==j:
                contador=contador+1
    return contador