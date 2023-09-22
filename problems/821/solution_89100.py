def fatorial(n):
    '''Dado um número n, retorna o seu fatorial.
    int -> int'''
    fats_n = list(range(1, n+1))
    acumul=1
    cont=0
    while cont < n:
        acumul = acumul*fats_n[cont]
        cont = cont + 1
    return acumul