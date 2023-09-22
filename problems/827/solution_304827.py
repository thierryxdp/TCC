def qtd_divisores(n):
    '''função que conta quantos divisores um número tem'''
    quantidade=0
    for numero in range(1,n+1):
        if n%numero==0:
            quantidade=quantidade+1
    return quantidade