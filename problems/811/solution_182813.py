def colchao(AxBxC,H,L):
    '''Função que, dada as medidas do colchão e da porta, determina se é possível que o colchão passe pela porta.
    list, int, int, --> boll'''
    if (AxBxC[1] and AxBxC[2]) > (H and L):
        return False
    else:
        return True