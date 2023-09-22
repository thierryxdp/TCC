def fatorial(n):
    '''Função que dado um número calcula o fatorial
    int->int
    '''
    i=0
    fat=1
    while n-i>1:
        fat*=n-i
        i=i+1
    return fat