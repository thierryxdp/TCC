def fatorial(n: int) -> int:
    

    i = 0
    
    while i < n:
        
        fatorial = i * n-i
        n = fatorial

        i = i + 1
        
    return fatorial