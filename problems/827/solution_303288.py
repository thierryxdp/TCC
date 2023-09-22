def qtd_divisores(n):
    '''qtd_divisores recebe um numero inteiro n e devolve a quantidade de divisores que esse número possui.
    Assume a n valores inteiros.
    int-->int'''
    divisores=0
    valores=range(1,n+1)
    for numero in valores:
        if n%numero==0:
            divisores=divisores+1
    return divisores