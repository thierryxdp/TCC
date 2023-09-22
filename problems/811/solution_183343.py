def colchao(medidas,H,L):
    '''Rassagem de um colchao atraves de uma porta com altura H e largura L
       parameters:etorna se é possivel a p
       H:altura
       L:largura
       medidadas: medidas do colchao, organizados em ordem crescente, com forma de um paralelepipedo
       list, int, int -> bool'''
    [A,B,C]=medidas
    if (A < L and B < H) or (A < L and C < H) or (B < L and C < H) or (B < L and A < H):
        return True
    else:
        return False