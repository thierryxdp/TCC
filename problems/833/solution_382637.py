def conta_numero(numero,matriz):
    ''' '''
    contador = 0
    for linha in matriz:
        for i in linha:
            if i == numero:
                contador+=1
    return contador