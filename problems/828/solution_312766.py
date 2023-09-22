def primo(n):
    """Verifica se um número inteiro é primo
    	int -> bool
        Parameters:
        n: Número a ser verificado
        
        Returns:
        Se o número n é primo ou não
    """
    div = []
    
    for i in range (1,n+1):
        if n%i == 0:
            div = div.append(i)
            
    return len(div)