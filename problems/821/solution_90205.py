def fatorial(n):
    """retorna o fatorial do numero dado. (int->int)"""
    
    i=1
    fat=n
    
	while i<n:
        fat=fat*i
        i+=1
        
    return fat