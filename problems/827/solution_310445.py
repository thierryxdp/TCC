def qtd_divisores(n):
    return('Divisores de',(n),' são:')
    for i in range(1, n+1):
        if n % i == 0:
            return ('{}'.format(i), end= ' ')