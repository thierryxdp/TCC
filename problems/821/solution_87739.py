def fatorial(x):
    '''Dado um número x, a função retorna o fatorial desse número
    float -> float'''
    
    i = 0 
    lista = ()
    while x > i:
        t = (x * (x-1),) 
        lista = lista + t
        x = x - 2
        i = i + 1
        
    return lista[0]