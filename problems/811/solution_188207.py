import math
def colchao (medidas, H, L):
    '''dada as medidas do colchao (da maior para a menor) e as da porta, retorna True se o colchao passa pela porta, caso contrario, retorna False
       : list, int, int -> bool
    '''
    [A, B, C] = medidas
    medidas[0]>medidas[1]>medidas[2]
    
    if math.sqrt((A**2)+(B**2)+(C**2)) =< H*L:
        return True
    else: 
        return False