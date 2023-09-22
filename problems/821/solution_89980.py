def fatorial(numero):
    '''Função que calcula e retorna o fatorial de um numero dado como
    entrada; int->int'''
    n=1
    fatorial=1
    while n!= numero:
        fatorial= fatorial* (n+1)
        n+=1
    return fatorial