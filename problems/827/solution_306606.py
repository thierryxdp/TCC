def qtd_divisores(n):
    
    divisores=()
    for i in range(n+1):
        if n/i%1:
            divisores+=(i,)
    return len(divisores)