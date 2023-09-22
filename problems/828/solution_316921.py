def primo(n):
    """Funçao que dado o número n, retorna se é um número primo ou não """
    d = 0
    for d in range(1, p):
        if n % d == 0:
            d = d + 1
            if d > 1:
                return False
            else:
                return True