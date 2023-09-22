def carros(pessoas, capacidade):
    ''
    s = int (pessoas/capacidade)
    if pessoas % capacidade == 0:
        return s
    elif pessoas % capacidade >= 1:
        return s + 1