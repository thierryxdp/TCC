def carros(num_pessoas, capacidade = 5):
    num_carros = num_pessoas / capacidade + 1
    return int(num_carros)