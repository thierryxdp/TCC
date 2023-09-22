def fatorial(n):
    """retorna o fatorial de um numero
    int -> int"""
    
    n_fatorial = 1
    
    for i in range(2,n+1):
        n_fatorial = n_fatorial*i
        return (n,n_fatorial)