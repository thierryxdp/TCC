def qtd_divisores(n):
    m= (n/2)
    for i in range(1,m):
        if (n % i) == 0:
            return i