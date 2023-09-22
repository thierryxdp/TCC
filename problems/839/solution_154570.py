from math import ceil
def carros(a, b=5):
    quantcarroamais = a % b
    quantidaderealamais = quantcarroamais / b
    quantcarro = int(a / b)
    return ceil(quantidaderealamais + quantcarro)