def num_bombons(dinheiro,preco_b):
    """Calcula e retorna quantos bobons será possível comprar com alguma quantia de dinheriso
       float, float, -> int"""
    return dinheiro//preco_b

def carros(num_passageiros, lugares=5):
    """Calcula e retorna quantos carros serão necessários
    int,int->int"""
    carros = num_passageiros//lugares
    return carros