def qtd_divisores(n):
    """Funcao calcula quantos divisores um numero dado: n tem """

    num_divisores = 0
    divisores = []

    for numero in range(1, n+1):
        if n%numero == 0:
            num_divisores += 1
            divisores.append(numero)

    return num_divisores, divisores