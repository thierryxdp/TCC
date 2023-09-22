def soma_h(n):
    '''soma e retorna a soma de 1 até 1/n
    	int->float'''
    
    i=0
    
    for j in range(n+1):
        
        i=i+1/j
        
    return round(i,2)