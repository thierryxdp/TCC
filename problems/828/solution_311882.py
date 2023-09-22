def primo(n:int) -> bool:
    """Função que irá identificar se um número dado como entrada é ou não um número primo.
        int -> bool
        
        Parameters:
        n: número inteiro positivo

        Returns:
        valor boleano True se o número for primo ou False se o número não for primo
    """

    for numero in range(2, n):
        if n % numero == 0:
       		n = n + 1
   		return False
    
    elif return True