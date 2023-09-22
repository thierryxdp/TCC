def qtd_divisores(n):
    i = 1
    div = []
    for i in range(1,n+1):
        if (n % i) == 0:
            return i