def primo(n):
    """Verifica se um número inteiro é primo
    	int -> bool
        Parameters:
        n: Número a ser verificado
        
        Returns:
        Se o número n é primo ou não
    """

    if(n<=1):
        return False
    for i in range(2,n):
        if(n%i == 0)
        	return False
    return True