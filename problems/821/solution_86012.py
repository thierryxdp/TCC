def fatorial(numero):
    """A funcao calcula o fatorial de um numero inteiro. int-->int."""
    numero = numero[0]
    fator = 1
    while numero > 0:
        fator = fator * numero
        numero = numero - 1
    return fator