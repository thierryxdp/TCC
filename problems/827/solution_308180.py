qtd_divisores(n):
    q = 0
    for i in range(1,n+1):
        if n % i == 0:
            q = q + 1
    return q