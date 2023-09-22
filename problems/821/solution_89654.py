def fatorial(n):
    '''funcao que dado um numero n retorna o valor
    do fatorial desse numero
    int->int '''
    proximo=1
    fatorial=1
    while proximo<n:
        fatorial = fatorial*proximo
        proximo= proximo +2
    return fatorial