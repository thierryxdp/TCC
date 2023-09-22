def fatorial(n):
    """funcao que recebe um numero e retorna o fatorial do mesmo
	int -> int"""
    
    fatorial = n
    
    while n > 1:
        fatorial = fatorial * (n-1)
        n -= 1
    
    return fatorial