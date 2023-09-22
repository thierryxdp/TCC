def primo(numero):
    """funcao que determina se um numero e primo ou nao"""
    for x in range(1,numero-1):
        if numero%x==0:
            return bool(False)
        else:
            return bool(True)