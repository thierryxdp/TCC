def fatorial(n):
    '''função que dado um número
    calcula o fatorial deste número
    int>>int''''
    proximo=1
    fatorial=n
    while n-proximo!=0:
        fatorial=fatorial*(n-proximo)
        proximo=proximo+1
    return fatorial