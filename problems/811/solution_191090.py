def colchao(medidas,H,L):
    '''
	função que calcula se o colchão passa ou não pela porta
    '''
    if medidas[1] > H and medidas[2] > L:
        return False
    elif medidas[1] > L and medidas[2] > H:
        return False
    else:
        return True