def conta_numero(numero,matriz):
    ''' '''
    contador=0
    for linha in range(matriz):
        for elemento in linha:
            if elemento==numero:
            	contador=contador+1
        else:
            	contador=contador
    return contador