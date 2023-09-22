def primo(num):
    if qtd_divisores(num) > 2 or 1:
        return False
    if qtd_divisores(num) == 2:
        return True