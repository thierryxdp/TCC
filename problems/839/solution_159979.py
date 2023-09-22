def carros(pessoas, capacidade=5):
    """Calcula quantos carros são necessarios dado um numero de pessoas.
       int, int -> float"""
    return round(pessoas/capacidade +0.5)