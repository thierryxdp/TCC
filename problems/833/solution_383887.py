def conta_numero(numero,matriz):
    conta = 0 
    for i in matriz:
        conta += list.count([i],numero)
    return conta