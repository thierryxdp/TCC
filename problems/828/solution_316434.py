def primo(num):
    """Essa função serve para dizer se o número é primo ou não
    int->bool"""
    if qtd_divisores(num) == 2:
        return True
    if qtd_divisores(num) > 2 or 1:
        return False

#primo(67) == True
#primo(12) == False
#primo(13) == True