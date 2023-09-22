def colchao(dimensoes,H,L):
    '''Retorna se o colção atravessará a porta da casa
    list,int,int -> bool'''
    if dimensoes[0]<=L and dimensoes[1]<=H:
        return True
    elif dimensoes[1]<=L and dimensoes[0]<=H:
        return True
    else:
        return False