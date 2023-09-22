def qtd_divisores(n):
    c=0
    
    for x in range(1,n+1):
        if n%x == 0:
            c += 1
    return c