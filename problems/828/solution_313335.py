def primo(n):
    """ Dado um número n, retorna se ele é primo ou não.
    int -> boolean
    """
    if(n <= 1):
        return False
    for i in range(2, n):
        if(not n % i):
            return False
    return True