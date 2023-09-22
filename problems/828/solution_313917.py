def primo(x):
    """Função que determina se um número é primo(True) ou não é primo(False)
    int -> bol"""
    fator = 2
    while x % fator != 0 and fator <= x/2:
        fator = fator + 1
    if x % fator == 0:
        return False
    else:
        return True