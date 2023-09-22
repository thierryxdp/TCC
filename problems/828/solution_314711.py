def primo(numero):
    """Funcao que retorna se o numero e primo ou nao
    int --> boolean"""
    for i  in range(1,numero):
        if not(numero % i == 0):
            return True
        elif numero == 2:
            return True
        else:
            return False