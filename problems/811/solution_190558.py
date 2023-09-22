def colchao(medidas,H,L):
    '''
    funcao utilizada para verificar se o colchao
    comprado de medidas (a,b e c) passa pela porta
    '''
    a,b,c=medidas
    if b<=H:
        return True
    elif b<=L:
        return True
    else:
        return False