def fatorial(x):
    '''Função que dado um numero inteiro calcula seu fatorial. int->int'''
    f=1
    for c in range(x,0,-1):
        f*= c
    return f