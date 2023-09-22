def colchao(medidas,H,L):
    '''função que define se o colchao passa ou não pela porta;
    list,int,int->bool'''
    if (medidas[0] and medidas[1]) or (medidas[0] and medidas[2])<H and L:
    	return True
    if medidas[1] or medidas[2]>H and L:
        return False
    else:
        return False