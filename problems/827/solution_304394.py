def qtd_divisores(n):        
    divisores=0
    for a in range(1,n):
        if (n % a == 0 ):
            divisores += a
            return divisores