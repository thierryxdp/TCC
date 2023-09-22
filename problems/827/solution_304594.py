def qtd_divisores(n):
    '''função que dado um numero conta a quantidade de divisores que esse número terá
    entrada:int
    saida:int'''
    divisores = 0
    for i in range(1,n+1):
        if n%i == 0:
            divisores = divisores + 1
    return divisores