def qtd_divisores (n):
    ''' retorna quantos divisores o número tem; entrada-> n; int->int'''
    c=0
    for x in range (1,n+1):
        if n % x == 0:
            c=c+1
    return c