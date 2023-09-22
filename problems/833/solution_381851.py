def conta_numero(numero,matriz):
    cont=0
    for e in matriz:
        for i in e:
            if i==numero:
                cont=cont+1
    return cont