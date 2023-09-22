def colchao(medidas, H, L):
    '''
       A -> largura
       B -> altura
       C -> profundidade
       list, int, int -> bool
    '''
    if medidas[0]*medidas[1] <= H*L:
        return True
    else:
        return False