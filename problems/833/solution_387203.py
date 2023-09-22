def conta_numero(numero,matriz):
    ''' '''
    vezes=0
    for i in matriz:
        for j in matriz:
            if i == numero:
            vezes+=1
    return vezes