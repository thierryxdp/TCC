def conta_numero(numero,matriz):
    '''
    
    '''
    quant=0
    for linha in matriz:
        quant=quant+list.count(linha,numero)
    return quant