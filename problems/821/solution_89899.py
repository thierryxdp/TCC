def fatorial(n):
    '''Retorna o fatorial do
    número n inserido
    int --> int'''
    i = 0
    mult = 1
    numero = n
    if n == 0:
        return 0
    while i < numero:
        mult = mult * n
        n = n-1
        i = i+1
    return mult