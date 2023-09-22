def qtd_divisores (n):
    s = 0
    for d in range(1,n+1):
        if n%d == 0:
            return s += d