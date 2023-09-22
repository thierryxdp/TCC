def primo(n):
    """Retorna se um número é primo ou não.
    Entrada: int
    Saída: bool
    """
    a = n
    if a == 2 and (a<=a-1):
        return True
    else:
        return False