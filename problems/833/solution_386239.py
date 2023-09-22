def conta_numero2(numero,matriz):
    k=0
    for i in matriz:
        for elemento in i:
            if elemento==numero:
                k=k+1
    return k