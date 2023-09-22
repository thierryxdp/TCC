def carros(a, b=5):
    quantcarro = a / b
    resto = a % b
    if quantcarro > 0:
        return int(quantcarro + resto -1)
    return int(quantcarro)