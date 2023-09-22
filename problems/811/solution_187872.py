def colchao (medidas, H, L):
    '''dada as medidas do colchao (da maior para a menor) e as da porta, retorna True se o colchao passa pela porta, caso contrario, retorna False
       : list, int, int -> bool
    '''
    medidas[0] = A
    medidas[1] = B
    medidas[2] = C
    if A > B and B > C:
        (A*B*C) < H*L
        return True
    else: 
        return False