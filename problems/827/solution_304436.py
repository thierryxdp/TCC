def qtd_divisores(n):
    divisores = 1
    for divisores in range(1,n+1):
         divisores = n//divisores
        divisores = len(divisores)
    return divisores