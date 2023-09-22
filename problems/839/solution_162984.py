def carros(pessoas, capacidade):
    ''
    capacidade = 5
    s = int (pessoas/capacidade)
    if pessoas % capacidade == 0:
        return s