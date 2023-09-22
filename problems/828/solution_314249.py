def primo(n):
    """Função que verifica se o número indicado e primero.
    Parametros: int->int"""
    for numero in range(2, n):
        if n % numero == 0:
            return False