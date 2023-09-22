def colchao(medidas, H, L):
    '''
       A -> largura
       B -> altura
       C -> profundidade
       list, int, int -> bool
    '''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if A*B <= H*L:
        return True
    else:
        return False