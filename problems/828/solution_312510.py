def primo(n):
    """Função que dado um número inteiro positivo n, retorna True se ele for primo e False se não for primo.
    int -> bool """

    divisores = 0

    for numero in range(1, n + 1):
        if n % numero == 0:
            divisores = divisores + 1


    if divisores == 2:
        return True

    else:
        return False