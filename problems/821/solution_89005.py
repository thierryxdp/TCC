def fatorial(n):
    
    anterior = []
    
    while n != 0:
        n = n - 1
        anterior += [n,]
        
    return prod(anterior)