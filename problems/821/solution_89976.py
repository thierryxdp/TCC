def fatorial(numero):
    '''Função que recebe um número e retorna o fatorial do mesmo.
    int->int'''
    i=1
    fatorial=1
    while i<=numero:
        fatorial = fatorial*i
        i+=1
    return fatorial