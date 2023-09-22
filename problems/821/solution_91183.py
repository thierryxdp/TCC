def fatorial(x):
    '''
    funcao que recebe um numero x
    e retorna seu fatorial
    int->int
    '''
    proximo=1
    calculo=1
    while proximo<=x:
        calculo=calculo*proximo
        proximo=proximo+1
    
    return calculo