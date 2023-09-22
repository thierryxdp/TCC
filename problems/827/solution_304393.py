def qtd_divisores(n):        
    divisores=0
    for a in range(2,n+1):
        if n%a==0:
            divisores= divisores+a
            return divisores