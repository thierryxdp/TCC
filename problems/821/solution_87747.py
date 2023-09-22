def fatorial(numero):
    '''retorna o fatorial de um numero'''
    i=numero
    fatorial=numero
    while i > 0:
        i = i-1
        fatorial = fatorial * i
    return fatorial