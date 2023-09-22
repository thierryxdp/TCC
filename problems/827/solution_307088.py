def qtd_divisores(n):
    x = 1
    k = 0
    while x < n + 1:
        if n%x==0:
            k = k +1
        x = x + 1
    return k