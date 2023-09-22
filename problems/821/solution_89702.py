def fatorial(n):
    '''funcao que retorna um aftorial.'''
    '''int=>int'''
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat
    return s