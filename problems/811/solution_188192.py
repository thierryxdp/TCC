import math
def colchao (medidas, H, L):
    '''dada as medidas do colchao (da maior para a menor) e as da porta, retorna True se o colchao passa pela porta, caso contrario, retorna False
       : list, int, int -> bool
    '''
    [A, B, C] = medidas
    medidas[0]>medidas[1]>medidas[2]
    
    if (A*B) < H*L:
        return True
    if (B*C) < H*L:
        return True
    if (C*A) < H*L:
        return True
    else: 
        return False