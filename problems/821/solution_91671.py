def fatorial(numero):
    '''Função que calcula o fatorial de um numero
    int->int'''
    i = 1
    x = 1
    while i<=numero:
        x = x*i
        i = i+1
    return x