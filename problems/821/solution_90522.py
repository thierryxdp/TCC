def fatorial(n):
    """Recebe um número e devolve como resultado seu fatorial;
    	int -> int"""
    fat=1
    while n!=1:
        fat=fat*n
        n=n-1
    return fat