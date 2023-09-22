def conta_numero(numero, matriz):
    '''
    '''
    
    contador = 0
    
    for linha in matriz:
        contador += linha.count(numero)
    
    return contador