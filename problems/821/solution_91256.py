def fatorial(n):
    '''
    Funcao que recebe um numero n. A funcao retorna o calculo do fatorial desse numero.
    int -> int
    '''
    resultado = 1
    con = 1
    while con<= n:
        resultado *=con
        con = con +1
    return resultado