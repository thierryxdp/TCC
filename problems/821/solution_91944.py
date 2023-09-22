def fatorial(numero):
    """def que ao dar um numero inteiro como entrada, retorna seu fatorial. int --> int"""
    fator = numero -1
    resultado = 1
    if numero < 1:
        return 1
    resultado = resultado*numero*(fator)
    while fator != 0:
        fator -= 1
        resultado = resultado*(fator)
    return resultado