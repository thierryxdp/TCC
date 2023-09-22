def carros(pessoas, capacidade=5):
    """Calcula o numero de carros dado a quantidade de pessoas e a capacidade caso o corro n for convencional
       int, int -> int"""
    if pessoas==capacidade:
        return pessoas//capacidade
    else:
        return round(pessoas/capacidade+0.5)