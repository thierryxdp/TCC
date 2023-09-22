def colchao(medidas,H,L):
    ''' funcao do colchao'''
    medidas.sort(reverse=True)
    if medidas[1]<=H:
        return True
    elif medidas[1]<L:
        return True
    else:
        return False