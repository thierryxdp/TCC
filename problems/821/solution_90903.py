def fatorial(numero):
    '''retorna o fatorial do numero
    int-> int'''
    fatorial=1
    while(numero>=1):
        fatorial=fatorial*numero
        numero=numero-1
    return fatorial