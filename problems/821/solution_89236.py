def fatorial(n):
    """ Dado um número retorna o fatorial deste número 
    int -> int """
    saida = 1
    while n>0:
        saida*=n
        n-=1
    return saida