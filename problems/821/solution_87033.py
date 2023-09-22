def fatorial(numero):
    """função que dado um número, calcule o fatorial deste número."""
    fat = numero
    while numero > 1:
        fat = fat * (numero - 1)
        numero -= 1
    return fat