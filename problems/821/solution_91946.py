def fatorial(numero):
    """def que ao dar um numero inteiro como entrada, retorna seu fatorial. int --> int"""
    fator = numero -1
    resultado = 1
    if numero < 1:
        return 1
    resultado = resultado*numero*(fator)
    while fator != 0:
        fator -= 1
        if fator == 0:
            return resultado
        resultado = resultado*(fator)
    return resultado