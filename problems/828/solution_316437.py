def primo(n):
    """Dado um número n,checa se ele é primo"""
    if qtd_divisores(n) == 2:
        return True
    else:
        return False