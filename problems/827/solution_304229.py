def qtd_divisores(n):
    
    k = 0
    
    for i in range(1, n + 1):
        if n % i ==0:
            k += 1
    
    return k