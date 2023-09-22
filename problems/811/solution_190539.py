def colchao(medidas,H,L):
    '''função que define se o colchao passa ou não pela porta;
    list,int,int->bool'''
    area_porta = H*L
    A_colchao1 = medidas[0]*medidas[1]
    A_colchao2 = medidas[0]*medidas[2]
    A_colchao3 = medidas[1]*medidas[2]
    if area_porta> A_colchao1 and A_colchao2 and A_colchao3:
        return True
    else:
        return False