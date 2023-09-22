def colchao(medidas,H,L):
    '''retorna se o colcao passa na porta;
    lista,int,int->bool'''
    if medidas[1]<=H or medidas[2]<=L:
        return True
    elif medidas[2]<=H or medidas[1]<=L:
        return True
    else:
        return False