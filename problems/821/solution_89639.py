def fatorial(n):
    '''funcao que dado um numero n retorna o valor
    do fatorial desse numero
    int->int '''
    proximo=1
    while proximo<n:
        fatorial =n*(n-proximo)
        proximo= proximo +1
    return fatorial