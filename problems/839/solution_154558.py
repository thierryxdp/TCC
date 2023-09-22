def carros(a, b=5):
    quantcarro = a / b
    if quantcarro >= 0:
        return int(quantcarro + 1)
    return int(quantcarro)