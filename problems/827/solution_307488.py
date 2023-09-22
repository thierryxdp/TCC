def qtd_divisores(n):
    '''Dado um númro inteiro n retorna a quantidade de divisores.
    int -> int'''
    acumul = 0
    cont = 1
    while cont <= n:
        if n%cont == 0:
            acumul += 1
        cont += 1
    return acumul