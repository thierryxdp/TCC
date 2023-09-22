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
    if (A > H and L) or (B > H and L) or (C > H and L):
        return False
    else:
        return True