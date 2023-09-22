def colchao(medidas:list,H,L):
    '''função que diz se da pra passar o móvel pela porta.list,float,float->bool'''
    if medidas[0]<=L and medidas[2]<=H:
        return True
    if medidas[0]<=H and medidas[2]<=L:
        return True
    if medidas[0]<=L and medidas[1]<=H:
        return True
    if medidas[0]<=H and medidas[1]<=L:
        return True
    if medidas[1]<=L and dimensoes[2]<=H:
        return True
    if medidas[1]<=H and medidas[2]<=L:
        return True
    else:
        return False