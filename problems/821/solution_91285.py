def fatorial(n):
    '''função que dado um número
    calcula o fatorial deste número
    int--->int
    ''''
    numseguinte=1
    fatorial=n
    while n-numseguinte!=0:
        fatorial=fatorial*(n-numseguinte)
        numseguinte=numseguinte+1
    return fatorial