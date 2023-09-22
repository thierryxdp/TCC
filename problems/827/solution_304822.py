def qtd_divisores(n: int):
    '''função que conta quantos divisores um número tem'''
    quantidade=0
    for numero in n:
        if numero%n==0:
            quantidade=quantidade+1
    return quantidade