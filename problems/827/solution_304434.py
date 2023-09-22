def qtd_divisores(n):
    divisores = 1
    for divisores in range(1,n+1):
        n//divisores
        divisores = len(divisores)
    return divisores