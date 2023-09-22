def conta_numero(numero,matriz):
    ''' '''
    contador=0
    i=0
    while i<len(matriz):
        contador= contador+ 1
        if matriz[i]==numero:
            contador= contador+ matriz.count(numero)
        i=i+1    
    return contador