def primo(n)
    """XXXXXXX"""
    divisores = 0
    for divisor in range(1, n):
        if numero % divisor == 0:
            divisores = divisores + 1
            if divisores > 1:
    if divisores > 1:
        return True
    else:
        return False