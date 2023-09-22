def fatorial(numero):
    '''int -> int'''
    '''retorna o fatorial do numero'''
    
    f = 1
    
    if numero == 0:
        return 1
    
    while numero >= 1:
        f = f*numero
        pass
    return f