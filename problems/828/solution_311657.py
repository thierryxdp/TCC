def primo(n):
    """ A funçao primo, dado um número inteiro positivo, verifica se este número é primo ou não
        
        Parameters:
            n = numero a ser analisado se é primo ou nao

        Testes:
            primo(10) = 4
            primo(4) = 3
            primo(3) = 1
            
        Returns:
            quantos divisores o número inserido tem.
            int --> int
    """
    for i in range(2,n):
        if n%i == 0:
            return False
        return True