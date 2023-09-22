def qtd_divisores(n):
    '''Dado um númeron, retorne o número de divisores desse número; int->int'''
    div=0
    for numero in range(1,n+1):
        if n%numero==0:
            div=div+1
    return div