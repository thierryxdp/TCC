def colchao(medidas, H, L):
    '''
       A -> profundidade
       B -> altura
       C -> largura
       list, int, int -> bool
    '''
    A = medidas[0]
    B = medidas[1]
    C = medidas[2]
    if B > H and L:
        return False
    elif C > H and L:
        return False
    else:
        return True