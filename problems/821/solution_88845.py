def fatorial(n):
    if n==0:
        return 0
    i=1
    x=1
    while i<n:
    	x=x+n*(n-1)
    	i=i+1    
    return x