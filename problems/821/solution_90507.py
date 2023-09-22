def fatorial(numero):
    """A função recebe como entrada um número inteiro e
    retorna o seu fatorial."""
    fatorial = 1
    while numero > fatorial:
        fatorial *= numero
        numero = numero - 1
    return fatorial