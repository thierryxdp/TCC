def fatorial (n):
    """Retorna o fatorial de um número n dado como entrada. int-> int"""
    i = 1  
    fatorial = n
    while i < n:
        fatorial = fatorial * (n-i) 
        i = i+1
    return fatorial