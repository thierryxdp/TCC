def fatorial(n):
    '''dado um inteiro n, retorna o fatorial desse numero; int -> int'''
    k = 1
    produto = 1
    while k < n:
        produto = produto*(k+1)
        k = k + 1
    return produto