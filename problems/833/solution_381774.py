def conta_numero(numero,matriz):
    T=0
    for c in matriz:
        if numero in c:
            T+=1
    return T