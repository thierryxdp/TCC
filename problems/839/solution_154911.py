#número de carros pra viagem
import math
def carros (pessoas,capacidade=5):
    """quantos carros são necessários pra viagem"""
    return math.ceil(pessoas/capacidade)