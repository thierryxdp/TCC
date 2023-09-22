def questaoimpossivel(dimensoes:list,H,L):
    '''função que diz se da pra passar o móvel pela porta.list,float,float->bool'''
    if dimensoes[0]<=L and dimensoes[2]<=H:
        return True
    if dimensoes[0]<=H and dimensoes[2]<=L:
        return True
    if dimensoes[0]<=L and dimensoes[1]<=H:
        return True
    if dimensoes[0]<=H and dimensoes[1]<=L:
        return True
    if dimensoes[1]<=L and dimensoes[2]<=H:
        return True
    if dimensoes[1]<=H and dimensoes[2]<=L:
        return True
    else:
        return False