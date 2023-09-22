def primo(n):
    """ A funçao primo, dado um número inteiro positivo, verifica se este número é primo ou não
        
        Parameters:
            n = numero a ser analisado se é primo ou nao

        Testes:
            primo(7) = True
            primo(10) = False
            primo(93) = False
            
        Returns:
            True se o número inserido é primo e False se não
            int --> bool
    """
    for i in range(2,n):
        if n%i == 0:
            return False
    return True