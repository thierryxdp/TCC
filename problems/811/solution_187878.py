def colchao (medidas, H, L):
    '''dada as medidas do colchao (da maior para a menor) e as da porta, retorna True se o colchao passa pela porta, caso contrario, retorna False
       : list, int, int -> bool
    '''
    [A, B, C] = medidas
     A > B and B > C:
    if (A*B*C) < H*L:
        return True
    else: 
        return False