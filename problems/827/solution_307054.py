def qtd_divisores(n):
    c = 0
    for i in range(n+1):
        if n%i == 0:
            c = c+1 
    return c