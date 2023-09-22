def colchao(ABC,H,L):
    import math
    diagonal_porta = math.sqrt((H**2)+(L**2))
    colchao = list(ABC)
    if diagonal_porta < colchao[1]:
        return true