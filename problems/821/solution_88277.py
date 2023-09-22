def fatorial(n: int) -> int:
    

    i = 1
    fatorial = 1
    
    while i < n+1:
        
        fatorial *= i

        i = i + 1
        
    return fatorial