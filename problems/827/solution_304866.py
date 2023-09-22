def qtd_divisores(n):
    p=0
    for div in range(1,n+1):
        if div%n==0:
    p= p + div
    return p