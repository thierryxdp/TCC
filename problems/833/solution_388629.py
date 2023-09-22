def conta_numero(numero,matriz): 
    x=0
    for e in matriz:
        x= x+list.count(e,numero)
    return x