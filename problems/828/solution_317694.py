def primo(n):
    """ Função que retorna se o número é primo(True)
    ou se não é primo(False).
    Entrada: int
    Saída: bool """
    for i in range(2,n):
        if n%i==0: 
            return False
    else:    
        return True