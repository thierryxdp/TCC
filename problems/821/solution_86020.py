def fatorial(lista):
    """A funcao calcula o fatorial de um numero de entrada, int-->int."""
    numero = lista[0]
    fator = 1
    while numero > 0:
        fator = fator * numero
        numero = numero - 1
    return fator