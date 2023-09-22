def primo(n):
    """Dado um número, verifica se é primo ou não"""
    for numero in range(2,n):
        if n%numero == 0:
            return False
        else:
            return True