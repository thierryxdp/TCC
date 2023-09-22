def primo(numero):
    """Funcao que retorna se o numero e primo ou nao
    int --> boolean"""
    for i  in range(1,numero):
        if numero % i == 0:
            return False
        elif numero % i != 0:
            return True