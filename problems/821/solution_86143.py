def fatorial(numero):
    ''' calcula o fatorial do numero de entrada
    int -> int'''
    v=1
    for fator in range(numero,1,-1):
        v=v*fator
    return v