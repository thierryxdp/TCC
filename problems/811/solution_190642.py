def colchao(medidas, H, L):
    '''
       A -> largura
       B -> altura
       C -> profundidade
       list, int, int -> bool
    '''
    medidas = [A,B,C]
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if medidas[0]*medidas[1] <= H*L:
        return True
    else:
        return False