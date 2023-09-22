def colchao(medidas,H,L):
    '''função que define se o colchao passa ou não pela porta;
    list,int,int->bool'''
    medidas = [A,B,C]
    if (medidas[0] and medidas[1]) or (medidas[1] and medidas[2]) or (medidas[0] and medidas[2])<H:
    	return True
    if (medidas[0] and medidas[1]) or (medidas[1] and medidas[2]) or (medidas[0] and medidas[2])<L:
        return True
    else:
        return False