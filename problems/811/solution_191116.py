def colchao(ABC,H,L):
    import math
    diagonal_porta = math.sqrt((H**2)+(L**2))
    colchao = [ABC]
    if diagonal_porta > colchao[1] and L > colchao[2]:
        return True