def fatorial(x):
    '''Escreva um numero. A funcao retorna o fatorial desse numero.
    int -> int'''
    i=1
    fatorial=x
    while x-i!=1:  #subtrai x de i ate ser igual a 1
        fatorial=fatorial*(x-i)
        i=i+1
    return fatorial