def colchao(medidas,H,L):
    '''calcular e retornar se o colchão passa pelas portas'''
    '''list, int, int -> bool'''
    
    if [medidas[0:1]] <= 100 and [medidas[2:4]] <= 200:
        return True
    
    else:
        return False