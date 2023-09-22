def fatorial(numero):
    '''funcao que calcula o fatorial de um numero
    int->int'''
    fatorial=1
    i=1

    while i <= numero:
        fatorial *= i
        i += 1
    return fatorial