def fatorial(numero):
    '''retorna o fatorial de um numero'''
    i=numero
    fatorial=numero
    while i > 0:
        fatorial = fatorial * i
        i = i-1
    return fatorial