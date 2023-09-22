def fatorial (n):
    ''' recebe um numero e retorna o seu fatorial
    int->int
    '''
    proximo=1
    num=n
    while proximo < n:
        num=num*proximo
        proximo=proximo+1
    return num