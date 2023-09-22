def fatorial(n):
    '''Esta e a funcao que dado um numero calcula o 
    fatorial deste numero'''
    fatorial = 1
    i = 2
    while i <= n:
        fatorial = fatorial * i
        i = i + 1
    return fatorial