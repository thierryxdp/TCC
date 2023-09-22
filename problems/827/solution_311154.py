def qtd_divisores(n):
        
    r = range(1, n+1)
    
    return len(filter(r, lambda x: n%x == 0))