def colchao(medidas,H,L):
    '''retorna se o colcao passa na porta;
    lista,int,int->bool'''
    if medidas[1]<=H:
        return True
    elif medidas[1]<=L:
        return True
    elif medidas[2]<=H:
        return True
    elif medidas[2]<=L
    else:
        return False