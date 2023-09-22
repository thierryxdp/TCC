def fatorial(n):
    
    """"Funçao que recebe um numero, calcula e retorna o fatorial do mesmo."""
    
    if n <= 1:
        
        return 1
    
    return n * fatorial(n - 1)