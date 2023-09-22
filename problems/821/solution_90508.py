def fatorial(numero):
    """A função recebe como entrada um número inteiro e
    retorna o seu fatorial."""

    fatorial = 1
    contador = 1

    while contador <= numero:
        fatorial *= contador
        contador += 1

    return fatorial