def fatorial(numero):
    """Funcao que dado um numero calcula o fatorial desse numero
    int -- float"""
    i = 1
    fatorial = 1
    while i < numero:
        fatorial = i * fatorial
    return fatorial