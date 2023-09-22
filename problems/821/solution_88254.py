def fatorial(n: int) -> int:
    
    a = [*range(1, n+1)]
    b = []
    i = 0
    
    while i < len(a):
        
        c = a[i] * a[i+1]
    	c = c + b
        i = i + 1
        
    return b