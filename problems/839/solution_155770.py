def carros(pessoas,capacidade=5):
    """Funçao que calcule a capacidade de transportar passageiros """
   veiculos = math.ceil(pessoas / capacidade) 
    return veiculos