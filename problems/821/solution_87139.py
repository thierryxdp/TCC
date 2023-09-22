def fatorial(n):
    """Calcula o fatorial de um número
    	int -> int
        Parameters:
        n: Número inicial
        
        Returns:
        A fatorial do número fornecido
    """
    
    i = 1
    fat = 1
    
    while i < n:
        i = i+1
        fat = fat*i
    
    return fat