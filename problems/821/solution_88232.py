def fatorial(n: int) -> int:
    
    a = [*range(1, n)]
    i = 0
    
    while i < len(a):
        
        a = [n,] + [n-1]
    	
        i = i + 1
        
    return a