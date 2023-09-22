def conta_numero(numero, matriz):
    '''
    '''
    
    contador = 0
    
    for i in matriz:
        contador += matriz[i].count(numero)
    
    return contador