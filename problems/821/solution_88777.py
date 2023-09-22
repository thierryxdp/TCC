def fatorial(numero):
    """Calcula o fatorial dado um inteiro. int -> int"""
    fator = 1
    u = 0
    while u < numero:
        u = u + 1
        if u != numero:
            fator = fator + fator * (numero-u)
    return fator