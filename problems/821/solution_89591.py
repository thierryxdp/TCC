def fatorial(l):
    '''faz o fatorial de uma lista de números(l)'''
    z = 0
    l1 = ()
    while z < len(l):
        l1 = l1 + (l-z)
        z = z + 1   
    return l1