def qtd_divisores(n):        
    divisores=0
    for count in range(1,n+1):
        if (n % count == 0):
            divisores += 1
    return divisores