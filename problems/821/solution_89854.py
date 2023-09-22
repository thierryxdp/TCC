def fatorial(n):
    '''funcao que dado um numero retorna seu fatorial'''
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
        return num