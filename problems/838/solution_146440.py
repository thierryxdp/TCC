def num_bombons (d, p):
    '''Calcula o total de bombons que é possível comprar.
    Dado o preço de cada bombom e o dinheiro disponível para comprá-los.'''
    return round(d//p), d % p