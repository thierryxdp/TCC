def soma_h(n):
    """Calcula o valor H,pela soma """
    numero = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        numero += inverso
    return round(numero, 2)