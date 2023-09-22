def colchao(medidas,H,L):
    '''
	função que calcula se o colchão passa ou não pela porta
    lista,int,int -> bool
    '''
    if (H or L) >= (medidas[1] or medidas[2]):
        return True
    else: 
        return False