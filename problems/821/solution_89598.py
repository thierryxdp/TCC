def fatorial(l):
    '''faz o fatorial de uma lista de números(l)'''
    return 1 if (l==1 or l==0) else l * fatorial(l - 1)