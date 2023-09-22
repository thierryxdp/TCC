def filtra_pares(t1):
    '''Calcula e retorna uma tupla apenas com os elementos pares e na mesma ordem da tupla original
    tupla -> tupla
    parameters:
    t1: tupla inicial'''
    a, b, c, d = t1
    nova_tupla = ()

    if(a%2 == 0):
        nova_tupla = nova_tupla + (a,)
    if(b%2 == 0):
        nova_tupla = nova_tupla + (b,)
    if(c%2 == 0):
        nova_tupla = nova_tupla + (c,)
    if(d%2 ==0):
        nova_tupla = nova_tupla + (d,)
    return nova_tupla