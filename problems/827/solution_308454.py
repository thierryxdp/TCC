def qtd_divisores(n):
    '''função que, dado um número, conta quantos divisores
    um número tem.
    int -> int'''
    tupla = ()
    for x in range(n):
        if n/x == n//x:
            tupla = tupla + (x,)
    return len(tupla)