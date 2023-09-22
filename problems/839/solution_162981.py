def carros(pessoas):
    ''
    capacidade = 5
    s = int (pessoas/capacidade)
    if pessoas % capacidade == 0:
        return s
    elif pessoas % capacidade >= 1:
        return s + 1