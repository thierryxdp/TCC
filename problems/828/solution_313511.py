def primo(n):
    """Função que irá identificar se um número dado como entrada é ou não um número primo.
        int -> bool"""
    for numero in range(2, n):
        if n % numero == 0:
            return False
            n = n + 1
    return True