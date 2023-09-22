def soma_h (n):
    '''função que dada um numero n retorna a soma de n 1/n termos; int->float'''
    h = 0
    for indice in range(1,n-1):
        h = h + (1/indice)
    return round(h,2)