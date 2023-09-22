def colchao(medidas,H,L):
    '''Funcao que calcula se o colchao vai passar pela porta
    list, int, int -> bool'''
    x = medidas[0]*medidas[1]/medidas[2]
    y = H*L
    if x <= y:
        return True
    else:
        return False