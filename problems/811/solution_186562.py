def colchao(medidas,H,L):
    '''Verifica se o colchão passa ou não entre a porta
    lista,int,int->str'''
    
    if medidas[1] >= H or medidas[1] >= L or medidas[2] >= H or medidas[2] >= L:
        return True
    else:
        return False