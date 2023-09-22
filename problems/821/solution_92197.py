def fatorial(numero):
    '''funcao que retorna o fatorial de um numero'''
    x=numero
    i=x
    r=x
    while i>0:
        r=i*(i-1)
        i=i-1
    return r