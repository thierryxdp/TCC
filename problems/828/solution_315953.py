def primo(x):
    """Função que dado um número inteiro positivo, verifica se esse número
    é primo ou não.
    """
    n = 2
    if n < x or x % n == 0:
        return False
    else:    
        return True