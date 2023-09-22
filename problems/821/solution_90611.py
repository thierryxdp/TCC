def fatorial(numero):
    '''Retorna o fatorial do numero dado;
    int->int'''
    i=1
    fatorial= numero
    while i<numero:
        fatorial=fatorial*i
        i+=1
    return fatorial