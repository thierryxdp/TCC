def qtd_divisores(n):
    '''Retorna a quantidade de divisores que o número n tem'''
    '''int->int'''
    divisores=0
    for x in range(1,n+1):
        if n%x==0:
            divisores=divisores+1
    return divisores