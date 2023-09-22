def conta_numero(numero,matriz):
    I=0
    for c in matriz:
        for i in matriz:
            if i==numero:
                I+=1
    return I