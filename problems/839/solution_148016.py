def carros(n_pessoas, capacidade = 5):
    if (n_pessoas % capacidade) == 0:
        return n_pessoas / capacidade
    else:
        return int(n_pessoas / capacidade) + 1