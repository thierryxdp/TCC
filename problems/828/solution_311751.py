def primo(n):
    """Funcao verifica se o numero dado: n e primo, e retorn um booleano
    caso for ou nao """

    divisores = []

    for numero in range(1, n+1):
        if n%numero == 0:
            divisores.append(numero)

    if len(divisores) > 2:
        return False
    else:
        return True