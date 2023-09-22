def fatorial(numero):
    '''Cacula o fatorial de um número.
    int --> int'''
    
    i = n
    j = 0
    resultado = 0
    
    while i > 0:
        resultado = resultado * (j+1)
        if i == numero:
            resultado = 1
        i -= 1
        j += 1
    return resultado