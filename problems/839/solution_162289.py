def carros(pessoas,capacidade=5):
    numero = pessoas%capacidade
    total = pessoa//capacidade
    if numero > 0:
        total += 1
    else:
        total = total
    return total