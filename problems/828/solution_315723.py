def primo(numero):
    """
    Essa função recebe um número inteiro positivo 
    e retorna se ele é primo ou não;
    int -> bool
    """
    for i in range(2, numero):
        if numero % i == 0:
            return False
    if numero <= 1:
        return False
    return True