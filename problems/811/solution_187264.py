def colchao(medidas,H,L):
    '''calcular e retornar se o colchão passa pelas portas'''
    '''list, int, int -> bool'''
    
    if medidas[0:1] <= H and medidas[2:4] <= L:
        return True
    
    else:
        return False