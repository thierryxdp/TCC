def carros(pessoas, capacidade=5):
    x = pessoas
    y = capacidade
    if(x % y != 0):
        return x//y + 1
    else:
        return x//y