def fatorial(numero):
    '''funcao que retorna o fatorial de um numero'''
    x=numero
    i=x-1
    r=x
    while i>0:
        r=r*(r-1)
        i=i-1
    return r