def fatorial(n: int) -> int:
    

    i = 0
    
    while i < n:
        
        fatorial = i * n
        n = fatorial

        i = i + 1
        
    return fatorial