def carros(pessoas, capacidade=5):
    if (pessoas/capacidade)%5 != 0:
        return pessoas//capacidade+1
    else:
        return pessoas/capacidade