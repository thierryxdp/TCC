def carros(a, b=5):
    quantcarroamais = a % b
    quantidaderealamais = quantcarroamais // b
    quantcarro = int(a / b)
    return quantidaderealamais + quantcarro