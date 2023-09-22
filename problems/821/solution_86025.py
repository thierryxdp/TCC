def fatorial (n):
    '''funcao que dado um numero 'n'
    calcula o seu fatorial; int -> int'''
    i = 0
    fatorial = n
    while n-i > 0:
        fatorial = fatorial * (n-i)
    return fatorial