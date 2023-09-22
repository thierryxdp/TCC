def carros (passageiros, capacidade=5):
    veiculos = passageiros//capacidade
    return math.ceil(veiculos)