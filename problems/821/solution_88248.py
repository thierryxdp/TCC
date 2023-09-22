def fatorial(n: int) -> int:
    
    a = [*range(1, n+1)]
    i = 0
    
    while i < len(a):
        
        b = a[i] * a[i-1]
    	
        i = i + 1
        
    return b