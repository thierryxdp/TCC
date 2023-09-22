def fatorial(numero):
    '''Função que dado um número retorna o seu fatorial
    int -> int'''
    fatorial = 1
    n = 0
    while n < numero:
        fatorial = fatorial * (numero - n)
        n = n + 1
    return fatorial