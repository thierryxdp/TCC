def colchao(medidas,H,L):
    '''calcular e retornar se o colchão passa pelas portas'''
    '''list, int, int -> bool'''
    
    if medidas[2] <= H and medidas[1] <= L:
        return True
    
    else:
        return False