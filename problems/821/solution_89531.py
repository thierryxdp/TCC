def fatorial(n):
    """calcula o fatorial do numero n dado (n!);
    int -> int"""
    f=1
    
    while n!=0:
        f=f*n
    	n=n-1
    
    return f