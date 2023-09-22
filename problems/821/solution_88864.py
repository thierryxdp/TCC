def fatorial(numero):
    """ Função que dado um número, calcula o fatorial desse
        número;
        int -> int"""
    i = 1
    fatorial = 1
    while i<=numero:
        fatorial = fatorial *(i+1)
        i = i+1
    return fatorial