def qtd_divisores(n):
    print('Divisores de',(n),' são:')
    for i in range(1, n+1):
        if n % i == 0:
            print ('{}'.format(i), end= ' ')