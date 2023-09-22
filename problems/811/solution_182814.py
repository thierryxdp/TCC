def colchao(AxBxC,H,L):
    '''Função que, dada as medidas do colchão e da porta, determina se é possível que o colchão passe pela porta.
    list, int, int, --> boll'''
    if (AxBxC[1] > H and AxBxC[1] > L and AxBxC[2] > (H or L)) or  (AxBxC[2] > H and AxBxC[2] > L and AxBxC[1] > (H or L)):
        return False
    else:
        return True