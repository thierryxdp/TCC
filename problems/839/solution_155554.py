from math import ceil
def carros(pessoas,capacidade=5):
    """Retorna o número exato de carros necessários para
       a viagem dados a quantidade de pessoas
       e a capacidade do veículo(caso seja diferente de 5)."""
    return ceil(pessoas//capacidade)