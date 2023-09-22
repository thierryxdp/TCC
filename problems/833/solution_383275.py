def conta_numero(numero,matriz):
    ''' '''
    contador=0
    i=0
    while i<len(matriz):
        if matriz[i]==numero:
            contador= contador+ 1
        i=i+1    
    return contador