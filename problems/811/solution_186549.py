def colchao (medidas,H,L):
    '''calcular se o colchão vai passar pela porta de medidas H e L, dadas sua altura e comprimento;
    list -> list'''
    if medidas [1]  <= H:
        return True
    if medidas [1] <= L:
        return True
    else:
        return False