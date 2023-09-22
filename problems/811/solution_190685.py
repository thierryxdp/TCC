def colchao(medidas,H,L):
    '''função que define se o colchao passa ou não pela porta;
    list,int,int->bool'''
    if (medidas[0] and medidas[1]) or (medidas[0] and medidas[2])<H or L:
    	return True
    elif medidas[1] and medidas[2]>H or L:
        return False
    elif medidas[1] and medidas[2]>H and L:
        return True
    else:
        return False