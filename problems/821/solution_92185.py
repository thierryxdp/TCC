def fatorial(n):
    '''A funcao recebe um numero n e retorna sua fatorial int->int'''
    fat=1
    ordem=2
    while ordem<n+1:
        fat=fat*ordem
        ordem=ordem+1
    return fat