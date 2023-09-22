def colchao(medidas,H,L):
    '''Determina se o colchão passa ou não pela porta
    (int,int,int),int,int->bool'''
    A=medidas[0]
    B=medidas[1]
    C=medidas[2]
    
    if B<=H:
        return True
    elif B<=L:
        return True
    else:
        return False