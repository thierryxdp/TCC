def primo(n):
    
    """Retorna se o numero n dado como entrada e primo ou nao
    int -> Bool
    """

    i = 1
    contador = 0

    while i <= n:
        if n % i == 0:
            contador = contador + 1
        i = i + 1
    if contador == 2:
        return True
    else:
        return False