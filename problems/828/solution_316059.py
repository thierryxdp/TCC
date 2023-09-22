def primo(n):
    """funcao que dado um numero n retorna se ele é primo ou não.
    int -> bool"""
    a = qtd_divisores(n)
    if a == 2:
        return True
    else:
        return False