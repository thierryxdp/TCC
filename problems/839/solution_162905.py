def carros(pessoas, capacidade=5):
    x = pessoas/capacidade
    y = pessoas//capacidade
    if(x < (y + 0.51)):
        return y + 1
    else:
        return round(x)