def faltante(n):
    x=0
    z=1
    while len(n)-1>=n[x]:
        if n[x] +1 <= n[x+1]:
            return n[x]+1
        
        x=x+1
        z=z+1
    if z==n[len(n)-1]:
        return z+1
    	elif z-1=len(n):
        return z+1
    
    else: return z