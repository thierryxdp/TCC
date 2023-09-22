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
            div = list.append(div,i)
                if len(div) == 2:
    return True