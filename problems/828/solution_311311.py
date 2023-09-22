def primo(numero):
    """Função que verifica se o número dado é primo ou não
    int -> bool"""
    if numero <= 1:
        return False
    for num in range(2, numero):
        if numero % num == 0:
            return False
    return True