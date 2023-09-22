def qtd_divisores(n):
        
    r = range(1, n+1)
    
    return len(filter(lambda x: n%x == 0, r))