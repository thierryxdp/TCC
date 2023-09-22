def carros(pessoas, capacidade):
    if capacidade == 5:
        return pessoas // 5
    elif capacidade < 5 or == 0:
        return pessoas // capacidade