def carros(pessoas, capacidade=5):
    """Calcula a quantidade de carros necessária dado o número de pessoas e, caso necessário a capacidade:
       int, int ->int"""
    return math.ceil(pessoas/capacidade)