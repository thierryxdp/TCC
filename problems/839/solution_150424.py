# int-> int
def carros(pessoas, capacidade=5):
    if (pessoas%capacidade == 0):
        return pessoas/capacidade
    else:
        return pessoas/capacidade + 1