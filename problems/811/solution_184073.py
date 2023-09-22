import math
def colchao(medidas,H,L):
    """Avalia as medidas de um colchão para saber se ele passa em uma porta"""
    A, B, C = medidas
    if math.sqrt(H**2 + L**2) > B and math.sqrt(H**2 + L**2) > C and math.sqrt(H**2 + L**2) > A or H>=B:
        return True
    else:
        return False