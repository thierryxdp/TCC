from math import ceil
def carros(p,c=5):
    """Calcula e retorna o número exato de carros necessários para esta viagem.
    dado como entrada o número de pessoas e a capacidade do carro caso seja diferente de 5. int/float,int/float->int/float"""
    return ceil(p/c)