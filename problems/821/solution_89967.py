def fatorial(valor):
    '''Dado um valor, a função calculará seu fatorial'''
    x = 1
    y = valor
    i = 0
    while i < valor:
        x=x*y
        y=y-1
        i=i+1
    return x