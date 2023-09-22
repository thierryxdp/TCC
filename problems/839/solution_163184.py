from math import ceil
def carros(x, y=5):
    """Função que calcula quantos carros serão usados em uma viagem, dados o número de pessoas que viajarão (x), em número inteiro, e a capacidade de cada carro (y), que deverá ser informada, em número inteiro, caso seja diferente de 5 passageiros.
    Valores de entrada: int, int
    Valor de saída: int"""
    return ceil(x/y)