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
    if B > H:
        return False
    if C > L:
        return False
    else:
        return True