def primo(n):
    """ 
    	Funcao que recebe um numero e retorna se ele é primo ou não;
    	int -> bool
    """
    for num in range(2, n):
        if n % num == 0:
            return False
        
    return True