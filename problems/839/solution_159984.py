def carros(pessoas, capacidade=5):
    """Calcula a quantidade de carro necessaria dado o numero de pessoas e a capacidade caso não seja convencional.
       int, int->int"""
    return round(int(pessoas/capacidade)+0.5)