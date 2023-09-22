def qtd_divisores(n):
    q = 0
    for a in range(1,n+1):
        if n % a == 0:
            q = q + 1
    return q