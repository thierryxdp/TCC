def fatorial(numero):
    '''funcao que retorna o fatorial de um numero'''
    i=numero
    r=numero
    while i>0:
        r=r*(r-1)
        i=i-1
    return r