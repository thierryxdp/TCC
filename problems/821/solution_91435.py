def fatorial(n):
    '''Calcula o fatorial de n. Assinatura: int->int'''
    res=1
    for x in range(n):
        res = res*(x+1)
    return res