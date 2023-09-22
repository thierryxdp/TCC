def fatorial(numero):
    """def que ao dar um numero inteiro como entrada, retorna seu fatorial. int --> int"""
    fator = numero -1
    if numero < 1:
        return 1
    while fator != 0:
        resultado = numero*(fator)
        fator -= 1
    return resultado