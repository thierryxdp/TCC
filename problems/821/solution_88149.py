def fatorial(numero):
    """calcula o fatorial ustilizando while"""
    fatorial = 1
    while numero >= 1:
        fatorial = fatorial * numero
        numero = numero - 1
    return (fatorial)