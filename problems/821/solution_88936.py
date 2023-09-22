def fatorial (n):
    '''funcao que calcule o fatorial deste numero'''
    if n == 0:
        return 1
    res = n
    while n > 2:
        n = n - 1 
        res = res * n
    return res