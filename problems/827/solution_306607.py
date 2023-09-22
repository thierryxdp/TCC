def qtd_divisores(n):
    
    divisores=()
    for i in range(n+1):
        if n/i%0:
            divisores+=(i,)
    return len(divisores)