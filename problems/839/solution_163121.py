def carros(pessoas, capacidade=5):
    if pessoas!=capacidade:
        return round(pessoas/capacidade+0.5)
    return 1