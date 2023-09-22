def conta_numero(numero,matriz):
    ''' '''
    qtd = 0
    for p in matriz:
        for q in p:
            if q == numero:
                qtd = qtd + 1
    return qtd