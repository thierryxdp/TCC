def primo(num):
    """Função que determina se um número é primo ou não.
signature: integer --> bool
"""
    for x in range (2, num, 1):
        num % x == 0