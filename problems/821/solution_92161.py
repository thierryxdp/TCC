def fatorial(n):
    '''Calcula o fatorial de n.
    int -> int'''

    fat = n-1
    
    while fat>0:
        n = n*fat
        fat = fat-1
    return n