def colchao(medidas,H,L):
    '''função que define se o colchao passa ou não pela porta;
    list,int,int->bool'''
    area_porta = H*L
    volume_colchao = medidas[0]*medidas[1]*medidas[2]
    if area_porta>volume_colchao:
        return True
    elif (medidas[0] and medidas[1]) or (medidas[1] and medidas[2]) or (medidas[0] and medidas[2])<H or L:
    	return True
    else:
        return False