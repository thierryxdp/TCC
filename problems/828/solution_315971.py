def primo(n):
    """Retorna se um número é primo ou não.
    Entrada: int
    Saída: bool
    """
    a = qtd_divisores(n)
    if a == 2:
        return True
    else:
        return False