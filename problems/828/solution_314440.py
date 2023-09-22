def primo(num):
    """Função que checa se o numero escolhido é primo ou não: int --> bool"""
    for div in range(num):
        if div > 1:
            if num % div == 0:
                return False
    return True