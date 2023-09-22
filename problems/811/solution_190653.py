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
    A and B > C
    if A or B > H and L:
        return False
    else:
        return True