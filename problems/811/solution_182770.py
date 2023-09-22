#definidas as dimensões do colchão em lista,  altura(H) da porta, e sua largura(L)
#afirma se é possível ou não que o colchão atravesse
def colchao(lista, H, L):
    A =lista[0] 
    B =lista[1] 
    C =lista[2] 
    '''A ->altura do colchão
    B ->comprimento do colchão
    C ->largura do colchão'''
    if B <=L and A <=H:
        return True
    if B <=H and A <=L:
        return True
    if C <=H and A <=L:
        return True
    else:
        return False