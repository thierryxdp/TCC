def fatorial (n):
    """Retorna o fatorial da entrada n; int->int"""
    
    cont = 1
    while n != 1:
		
        cont *= n
       
        n -= 1
    return cont