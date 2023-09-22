def qtd_divisores(n):
    '''Recebe um número natural e rotorna a
    quantidade de divisores que esse número 
    tem; int -> int'''
    divisores = []
    for i in range(n+1):
        if n // i == 0:
            divisores += [i]
    return len(divisores)