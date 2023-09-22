def qtd_divisores(n):
    '''dado um numero n, retorna quantos divisores este numero tem;
    int->int'''
    divisores=0
    for x in range(1,n+1):
        if n%x==0:
            divisores=divisores+1
    return divisores