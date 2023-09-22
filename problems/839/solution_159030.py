def carros(pessoas, capacidade=5):
    Ncarros = pessoas//capacidade
    if pessoas%capacidade > 0:
        Ncarros = Ncarros + 1
        
    return Ncarros