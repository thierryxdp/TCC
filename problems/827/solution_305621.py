def qtd_divisores(n):
    s = 0
    for i in range(1,n+1):
        if n % i==0:
            s += 1

    return s