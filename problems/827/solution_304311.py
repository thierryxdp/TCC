def qtd_divisores(n):
    '''A função recebe um número e retorna a quantidade de divisores que esse número tem.
    Parâmetro de entrada: int
    Valor de retorno: int'''
    divisores=0
    for numero in range(1,n+1):
        if n%numero==0:
            divisores=divisores+1
    return divisores